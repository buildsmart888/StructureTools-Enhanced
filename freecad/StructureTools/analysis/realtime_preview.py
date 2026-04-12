# -*- coding: utf-8 -*-
"""
Real-Time Analysis Preview

FreeCAD document observer that triggers lightweight analysis updates
in real-time as the user modifies structural elements (beam lengths,
support positions, loads). Uses debouncing and caching to provide
responsive feedback without blocking the UI.

Integration:
    from .realtime_preview import RealtimePreview
    preview = RealtimePreview()
    preview.start()   # Begin watching document changes
    preview.stop()    # Stop watching
"""

import time
import threading
from typing import Dict, Optional, Callable, Any

try:
    import FreeCAD as App
    HAS_FREECAD = True
except ImportError:
    HAS_FREECAD = False


class RealtimePreview:
    """Watches FreeCAD document for structural changes and triggers re-analysis.

    Features:
        - Debounced re-analysis (avoids running on every keystroke)
        - Background thread for analysis to keep UI responsive
        - Result caching (skips re-analysis if nothing changed)
        - Configurable update interval
    """

    def __init__(
        self,
        debounce_ms: int = 500,
        auto_start: bool = False,
        on_result: Optional[Callable] = None,
    ):
        """
        Args:
            debounce_ms: Minimum interval between analyses (milliseconds).
            auto_start: Whether to start watching immediately.
            on_result: Callback invoked with analysis results dict.
        """
        self.debounce_ms = debounce_ms
        self.on_result = on_result
        self._observer = None
        self._timer = None
        self._last_hash = None
        self._running = False
        self._lock = threading.Lock()

        if auto_start and HAS_FREECAD:
            self.start()

    def start(self):
        """Start observing the active document."""
        if not HAS_FREECAD:
            return
        if self._running:
            return

        self._running = True
        self._observer = _DocumentObserver(self._on_change)

        if App.ActiveDocument:
            App.ActiveDocument.addObserver(self._observer)

    def stop(self):
        """Stop observing."""
        self._running = False
        if self._timer:
            self._timer.cancel()

        if HAS_FREECAD and App.ActiveDocument and self._observer:
            try:
                App.ActiveDocument.removeObserver(self._observer)
            except Exception:
                pass
        self._observer = None

    def _on_change(self, obj_name: str):
        """Called when a document object changes."""
        if not self._running:
            return

        # Cancel any pending timer
        if self._timer:
            self._timer.cancel()

        # Debounce: schedule analysis after delay
        self._timer = threading.Timer(
            self.debounce_ms / 1000.0,
            self._run_analysis,
        )
        self._timer.daemon = True
        self._timer.start()

    def _run_analysis(self):
        """Run lightweight analysis in background."""
        with self._lock:
            if not self._running:
                return

            try:
                doc = App.ActiveDocument
                if not doc:
                    return

                # Compute hash of relevant structural state
                state_hash = self._compute_state_hash(doc)
                if state_hash == self._last_hash:
                    return  # Nothing changed

                self._last_hash = state_hash

                # Run a lightweight analysis
                result = self._quick_analysis(doc)

                if self.on_result and result:
                    self.on_result(result)

            except Exception as e:
                if HAS_FREECAD:
                    App.Console.PrintWarning(
                        f"Realtime preview: {e}\n"
                    )

    def _compute_state_hash(self, doc) -> str:
        """Hash relevant structural properties for change detection."""
        parts = []
        for obj in doc.Objects:
            proxy_type = getattr(obj, 'Proxy', None)
            if proxy_type is None:
                continue
            type_name = type(proxy_type).__name__
            if type_name in ('StructuralBeam', 'StructuralColumn', 'StructuralNode'):
                # Hash position/length/section
                if hasattr(obj, 'Placement'):
                    p = obj.Placement.Base
                    parts.append(f"{obj.Name}:{p.x:.2f},{p.y:.2f},{p.z:.2f}")
                if hasattr(obj, 'Length'):
                    parts.append(f"L:{obj.Length:.2f}")

        return "|".join(sorted(parts))

    def _quick_analysis(self, doc) -> Optional[Dict]:
        """Run a simplified analysis for preview purposes.

        Returns a dict with estimated reactions, max moment, max deflection.
        """
        # Collect beams and loads for quick estimate
        beams = []
        for obj in doc.Objects:
            proxy = getattr(obj, 'Proxy', None)
            if proxy and type(proxy).__name__ == 'StructuralBeam':
                beams.append(obj)

        if not beams:
            return None

        # Simple preview: assume each beam is simply supported
        preview_results = {}
        for beam in beams:
            L = getattr(beam, 'Length', 0)
            if L <= 0:
                continue

            E = getattr(beam, 'E', 200000)  # MPa or ksi
            I = getattr(beam, 'Ix', 100)

            # Estimate uniform load from self-weight
            w = getattr(beam, 'self_weight_per_length', 0)
            if w == 0:
                w = 1.0  # Default placeholder

            M_max = w * L ** 2 / 8
            V_max = w * L / 2
            delta_max = 5 * w * L ** 4 / (384 * E * I) if E * I > 0 else 0

            preview_results[beam.Name] = {
                'M_max': M_max,
                'V_max': V_max,
                'delta_max': delta_max,
                'length': L,
            }

        return preview_results


class _DocumentObserver:
    """FreeCAD document observer that triggers a callback on changes."""

    def __init__(self, callback: Callable):
        self._callback = callback

    def slotChangedObject(self, obj, prop):
        """Called when any object property changes."""
        self._callback(obj.Name if hasattr(obj, 'Name') else '')

    def slotCreatedObject(self, obj):
        self._callback(obj.Name if hasattr(obj, 'Name') else '')

    def slotDeletedObject(self, obj):
        self._callback(obj.Name if hasattr(obj, 'Name') else '')

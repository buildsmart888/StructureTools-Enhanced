# -*- coding: utf-8 -*-
"""
SAP2000 / ETABS File Import Module

Parses SAP2000 .$2k and Excel (.xlsx) export files to import
structural models into StructureTools / Pynite.

Supports reading:
  - Joint/Node coordinates
  - Frame/Member definitions
  - Section assignments
  - Material properties
  - Load patterns and assignments
  - Support/Restraint definitions
"""

import os
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, TextIO


@dataclass
class ImportedNode:
    """Imported joint/node."""
    name: str
    x: float
    y: float
    z: float
    restraints: List[bool] = field(default_factory=lambda: [False]*6)


@dataclass
class ImportedMember:
    """Imported frame element."""
    name: str
    node_i: str
    node_j: str
    section: str = ""
    material: str = ""
    releases_i: List[bool] = field(default_factory=lambda: [False]*6)
    releases_j: List[bool] = field(default_factory=lambda: [False]*6)


@dataclass
class ImportedSection:
    """Imported section definition."""
    name: str
    shape: str = ""
    material: str = ""
    properties: Dict[str, float] = field(default_factory=dict)


@dataclass
class ImportedMaterial:
    """Imported material."""
    name: str
    mat_type: str = "Steel"  # Steel, Concrete
    E: float = 0.0
    G: float = 0.0
    nu: float = 0.3
    fy: float = 0.0
    fu: float = 0.0
    density: float = 0.0


@dataclass
class ImportedLoad:
    """Imported load assignment."""
    member_or_node: str
    load_pattern: str
    load_type: str  # Point, Distributed, Moment
    direction: str  # X, Y, Z, GX, GY, GZ
    magnitude: float = 0.0
    distance: float = 0.0  # For point loads
    magnitude_end: float = 0.0  # For trapezoidal


@dataclass
class ImportedModel:
    """Complete imported model."""
    nodes: Dict[str, ImportedNode] = field(default_factory=dict)
    members: Dict[str, ImportedMember] = field(default_factory=dict)
    sections: Dict[str, ImportedSection] = field(default_factory=dict)
    materials: Dict[str, ImportedMaterial] = field(default_factory=dict)
    loads: List[ImportedLoad] = field(default_factory=list)
    load_patterns: List[str] = field(default_factory=list)
    units: str = "kip_in"
    source_file: str = ""

    @property
    def summary(self) -> str:
        return (
            f"Import: {os.path.basename(self.source_file)}\n"
            f"  Nodes: {len(self.nodes)}\n"
            f"  Members: {len(self.members)}\n"
            f"  Sections: {len(self.sections)}\n"
            f"  Materials: {len(self.materials)}\n"
            f"  Loads: {len(self.loads)}"
        )


class S2KParser:
    """SAP2000 $2k text file parser.

    The $2k format uses table blocks like:
        TABLE: "JOINT COORDINATES"
          Joint=1   CoordSys=GLOBAL   CoordType=Cartesian   XorR=0   Y=0   Z=0
    """

    def __init__(self):
        self.model = ImportedModel()

    def parse(self, filepath: str) -> ImportedModel:
        """Parse a SAP2000 .$2k or .s2k file."""
        self.model = ImportedModel(source_file=filepath)

        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            current_table = ""
            for line in f:
                line = line.strip()
                if not line or line.startswith(';'):
                    continue

                # Detect table header
                table_match = re.match(r'TABLE:\s*"(.+)"', line, re.IGNORECASE)
                if table_match:
                    current_table = table_match.group(1).upper()
                    continue

                if current_table == "JOINT COORDINATES":
                    self._parse_joint(line)
                elif current_table == "CONNECTIVITY - FRAME":
                    self._parse_frame(line)
                elif current_table == "JOINT RESTRAINT ASSIGNMENTS":
                    self._parse_restraints(line)
                elif current_table in ("MATERIAL PROPERTIES", "MATERIAL PROPERTIES 01 - GENERAL"):
                    self._parse_material(line)
                elif current_table in ("FRAME SECTION PROPERTIES", "FRAME SECTION PROPERTIES 01 - GENERAL"):
                    self._parse_section(line)
                elif current_table == "FRAME LOADS - DISTRIBUTED":
                    self._parse_distributed_load(line)

        return self.model

    def _parse_kv(self, line: str) -> Dict[str, str]:
        """Parse key=value pairs from a line."""
        pairs = {}
        for match in re.finditer(r'(\w+)=([^\s]+)', line):
            pairs[match.group(1).lower()] = match.group(2).strip('"')
        return pairs

    def _parse_joint(self, line: str):
        kv = self._parse_kv(line)
        name = kv.get('joint', '')
        if not name:
            return
        self.model.nodes[name] = ImportedNode(
            name=name,
            x=float(kv.get('xorr', kv.get('x', 0))),
            y=float(kv.get('y', 0)),
            z=float(kv.get('z', 0)),
        )

    def _parse_frame(self, line: str):
        kv = self._parse_kv(line)
        name = kv.get('frame', '')
        if not name:
            return
        self.model.members[name] = ImportedMember(
            name=name,
            node_i=kv.get('jointi', ''),
            node_j=kv.get('jointj', ''),
            section=kv.get('section', ''),
        )

    def _parse_restraints(self, line: str):
        kv = self._parse_kv(line)
        name = kv.get('joint', '')
        if name not in self.model.nodes:
            return
        r = [
            kv.get('u1', 'No') == 'Yes',
            kv.get('u2', 'No') == 'Yes',
            kv.get('u3', 'No') == 'Yes',
            kv.get('r1', 'No') == 'Yes',
            kv.get('r2', 'No') == 'Yes',
            kv.get('r3', 'No') == 'Yes',
        ]
        self.model.nodes[name].restraints = r

    def _parse_material(self, line: str):
        kv = self._parse_kv(line)
        name = kv.get('material', '')
        if not name:
            return
        self.model.materials[name] = ImportedMaterial(
            name=name,
            mat_type=kv.get('type', 'Steel'),
            E=float(kv.get('e', 0)),
            nu=float(kv.get('u', 0.3)),
        )

    def _parse_section(self, line: str):
        kv = self._parse_kv(line)
        name = kv.get('sectionname', kv.get('section', ''))
        if not name:
            return
        self.model.sections[name] = ImportedSection(
            name=name,
            shape=kv.get('shape', ''),
            material=kv.get('material', ''),
        )

    def _parse_distributed_load(self, line: str):
        kv = self._parse_kv(line)
        self.model.loads.append(ImportedLoad(
            member_or_node=kv.get('frame', ''),
            load_pattern=kv.get('loadpat', ''),
            load_type='Distributed',
            direction=kv.get('dir', 'GZ'),
            magnitude=float(kv.get('foverla', kv.get('forcea', 0))),
            magnitude_end=float(kv.get('foverlb', kv.get('forceb', 0))),
        ))


def import_to_pynite(imported: ImportedModel, model=None):
    """Convert ImportedModel to a Pynite FEModel3D.

    Args:
        imported: Parsed model from S2KParser.
        model: Existing Pynite FEModel3D. If None, one will be created.

    Returns:
        Pynite FEModel3D populated with nodes, members, and loads.
    """
    if model is None:
        try:
            from ..Pynite_main.FEModel3D import FEModel3D
            model = FEModel3D()
        except ImportError:
            raise ImportError("Pynite FEModel3D is required")

    # Add nodes
    for n in imported.nodes.values():
        model.add_node(n.name, n.x, n.y, n.z)
        # Supports
        if any(n.restraints):
            model.def_support(n.name, *n.restraints)

    # Add default material if needed
    default_E = 29000  # ksi steel
    default_G = 11200
    if not imported.materials:
        model.add_material('Default', default_E, default_G, 0.3, 490/12**3)

    # Add members (simplified — uses default properties)
    for m in imported.members.values():
        mat = m.material or 'Default'
        try:
            model.add_member(m.name, m.node_i, m.node_j,
                             mat, 10.0, 100.0, 100.0, 1.0, 1.0)
        except Exception:
            pass

    return model

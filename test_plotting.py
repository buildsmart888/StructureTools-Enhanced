"""
Test script to verify matplotlib functionality in FreeCAD.
This script should be run from within FreeCAD's Python console.
"""

def test_matplotlib_availability():
    """Test if matplotlib is available and working."""
    try:
        import matplotlib
        matplotlib.use('Qt5Agg')  # Use Qt5Agg backend for FreeCAD
        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
        from matplotlib.figure import Figure
        
        print("✅ Matplotlib is available")
        print(f"Matplotlib version: {matplotlib.__version__}")
        print(f"Matplotlib backend: {matplotlib.get_backend()}")
        
        # Test creating a simple figure
        fig = Figure(figsize=(5, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
        ax.set_title("Test Plot")
        
        print("✅ Matplotlib figure creation successful")
        return True
        
    except ImportError as e:
        print(f"❌ Matplotlib not available: {e}")
        return False
    except Exception as e:
        print(f"❌ Error with matplotlib: {e}")
        return False

def test_pyside_integration():
    """Test if PySide integration with matplotlib works."""
    try:
        from PySide2 import QtWidgets
        import matplotlib
        matplotlib.use('Qt5Agg')
        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
        from matplotlib.figure import Figure
        
        # Create a simple Qt application
        app = QtWidgets.QApplication.instance()
        if app is None:
            app = QtWidgets.QApplication([])
        
        # Create a widget with a matplotlib plot
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        fig = Figure(figsize=(5, 3), dpi=100)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
        ax.set_title("PySide + Matplotlib Integration Test")
        
        layout.addWidget(canvas)
        widget.setLayout(layout)
        
        print("✅ PySide + Matplotlib integration successful")
        return True
        
    except Exception as e:
        print(f"❌ Error with PySide + Matplotlib integration: {e}")
        return False

if __name__ == "__main__":
    print("Testing plotting capabilities for StructureTools...")
    print("=" * 50)
    
    matplotlib_ok = test_matplotlib_availability()
    pyside_ok = test_pyside_integration()
    
    print("\n" + "=" * 50)
    print("TEST SUMMARY:")
    print(f"Matplotlib Availability: {'✅ PASS' if matplotlib_ok else '❌ FAIL'}")
    print(f"PySide Integration: {'✅ PASS' if pyside_ok else '❌ FAIL'}")
    print(f"Overall Plotting Support: {'✅ AVAILABLE' if matplotlib_ok and pyside_ok else '❌ NOT AVAILABLE'}")
    print("=" * 50)
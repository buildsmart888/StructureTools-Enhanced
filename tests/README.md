# StructureTools Testing Framework

## Comprehensive Test Suite for Professional Workbench

This directory contains the complete testing framework for StructureTools workbench.

### 🧪 **Test Structure**

```
tests/
├── unit/                    # Unit tests for individual components
│   ├── objects/            # Custom Document Object tests
│   ├── analysis/           # Analysis engine tests
│   ├── ui/                 # Task panel and UI tests
│   └── integration/        # FreeCAD integration tests
├── integration/            # Integration tests
│   ├── workbench/         # Multi-workbench integration
│   ├── workflows/         # End-to-end workflow tests
│   └── performance/       # Performance and scalability tests
├── fixtures/              # Test data and models
│   ├── models/           # Sample structural models
│   ├── materials/        # Test material libraries
│   └── sections/         # Test section databases
├── benchmarks/           # Performance benchmarks
└── utils/               # Test utilities and helpers
```

### 🎯 **Testing Standards**

#### **Coverage Requirements:**
- **Minimum:** 90% line coverage for new code
- **Target:** 95% line coverage for critical components
- **Documentation:** All test functions must have docstrings

#### **Test Categories:**

**Unit Tests** (tests/unit/)
- Test individual classes and functions in isolation
- Mock external dependencies (FreeCAD API, file system)
- Fast execution (<1s per test)
- No GUI interaction required

**Integration Tests** (tests/integration/)
- Test component interactions
- Use real FreeCAD environment
- Test complete workflows
- May require GUI components

**Performance Tests** (tests/benchmarks/)
- Large model handling (1000+ elements)
- Analysis speed benchmarks
- Memory usage validation
- Scalability testing

### 🛠️ **Running Tests**

#### **Prerequisites:**
```bash
# Install test dependencies
pip install pytest pytest-cov pytest-mock freecad-stubs

# Set up FreeCAD path (if needed)
export FREECAD_PATH="/path/to/freecad"
```

#### **Test Commands:**

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=freecad.StructureTools --cov-report=html

# Run specific test category
pytest tests/unit/
pytest tests/integration/

# Run performance benchmarks
pytest tests/benchmarks/ --benchmark-only

# Run tests for specific module
pytest tests/unit/objects/test_structural_material.py

# Run with verbose output
pytest -v

# Run with parallel execution
pytest -n auto
```

### 📊 **Test Configuration**

#### **pytest.ini**
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --strict-markers
    --strict-config
    --cov=freecad.StructureTools
    --cov-branch
    --cov-report=term-missing
markers =
    unit: Unit tests
    integration: Integration tests
    performance: Performance tests
    slow: Slow-running tests
    gui: Tests requiring GUI
```

### 🧪 **Writing Tests**

#### **Unit Test Example:**
```python
# tests/unit/objects/test_structural_material.py
import pytest
from unittest.mock import Mock, patch
from freecad.StructureTools.objects.StructuralMaterial import StructuralMaterial

class TestStructuralMaterial:
    """Test suite for StructuralMaterial class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.mock_obj = Mock()
        self.material = StructuralMaterial(self.mock_obj)
    
    def test_material_initialization(self):
        """Test material object initialization."""
        assert self.material.Type == "StructuralMaterial"
        assert self.mock_obj.Proxy == self.material
    
    def test_poisson_ratio_validation(self):
        """Test Poisson ratio validation."""
        # Valid range
        self.mock_obj.PoissonRatio = 0.3
        self.material.onChanged(self.mock_obj, "PoissonRatio")
        assert self.mock_obj.PoissonRatio == 0.3
        
        # Invalid range - should be corrected
        self.mock_obj.PoissonRatio = 1.5
        self.material.onChanged(self.mock_obj, "PoissonRatio")
        assert self.mock_obj.PoissonRatio == 0.3  # Reset to default
    
    @patch('freecad.StructureTools.objects.StructuralMaterial.App.Console')
    def test_invalid_poisson_ratio_warning(self, mock_console):
        """Test warning message for invalid Poisson ratio."""
        self.mock_obj.PoissonRatio = -0.1
        self.material.onChanged(self.mock_obj, "PoissonRatio")
        mock_console.PrintWarning.assert_called_once()
```

#### **Integration Test Example:**
```python
# tests/integration/workflows/test_beam_analysis.py
import pytest
import FreeCAD as App
from freecad.StructureTools.objects.StructuralBeam import StructuralBeam

@pytest.mark.integration
class TestBeamAnalysisWorkflow:
    """Test complete beam analysis workflow."""
    
    def setup_method(self):
        """Create test document."""
        self.doc = App.newDocument("TestBeam")
    
    def teardown_method(self):
        """Clean up test document."""
        App.closeDocument(self.doc.Name)
    
    def test_simple_beam_analysis(self):
        """Test analysis of a simple supported beam."""
        # Create beam
        beam = self.doc.addObject("App::DocumentObjectGroupPython", "TestBeam")
        StructuralBeam(beam)
        
        # Set properties
        beam.Material = self.create_test_material()
        beam.Section = self.create_test_section()
        beam.Length = 6000  # mm
        
        # Apply loads
        self.apply_test_loads(beam)
        
        # Run analysis
        results = self.run_analysis(beam)
        
        # Verify results
        assert results is not None
        assert 'displacements' in results
        assert 'moments' in results
        
        # Check maximum deflection is within limits
        max_deflection = max(abs(d) for d in results['displacements'])
        assert max_deflection < beam.Length / 250  # L/250 limit
```

### 📈 **Performance Testing**

#### **Benchmark Example:**
```python
# tests/benchmarks/test_large_model_performance.py
import pytest
from freecad.StructureTools.analysis.LinearAnalysis import LinearAnalysis

class TestLargeModelPerformance:
    """Performance tests for large structural models."""
    
    @pytest.mark.performance
    def test_1000_element_analysis_time(self, benchmark):
        """Test analysis time for 1000-element model."""
        model = self.create_large_model(num_elements=1000)
        analysis = LinearAnalysis(model)
        
        result = benchmark(analysis.run_analysis)
        
        # Analysis should complete within 30 seconds
        assert benchmark.stats.median < 30.0
        assert result['converged'] is True
    
    @pytest.mark.performance
    def test_memory_usage_large_model(self):
        """Test memory usage for large models."""
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss
        
        # Create large model
        model = self.create_large_model(num_elements=5000)
        analysis = LinearAnalysis(model)
        analysis.run_analysis()
        
        final_memory = process.memory_info().rss
        memory_increase = (final_memory - initial_memory) / (1024 * 1024)  # MB
        
        # Memory increase should be reasonable (<500MB for 5000 elements)
        assert memory_increase < 500
```

### 🎯 **Continuous Integration**

#### **GitHub Actions Workflow:**
```yaml
# .github/workflows/tests.yml
name: StructureTools Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10]
        freecad-version: [0.21, 0.22]
    
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install FreeCAD
      run: |
        sudo add-apt-repository ppa:freecad-maintainers/freecad-stable
        sudo apt-get update
        sudo apt-get install freecad-python3
    
    - name: Install dependencies
      run: |
        pip install -r requirements-test.txt
    
    - name: Run tests
      run: |
        pytest --cov=freecad.StructureTools --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
```

### 📊 **Test Reporting**

- **Coverage Reports:** Generated in `htmlcov/` directory
- **Performance Reports:** Benchmark results in `benchmarks/` directory
- **CI Reports:** Available in GitHub Actions
- **Quality Gates:** Enforced minimum coverage and performance thresholds

---

**For more information:** See [Testing Guidelines](../docs/developer-guide/testing.md)
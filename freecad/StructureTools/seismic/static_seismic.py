"""
Static Seismic Analysis Module
==============================

This module provides functionality for static seismic analysis including:
- Story forces distribution according to various methods
- Vertical component calculation
- Integration with the story_forces.py module
- Visualization of story forces distribution
"""

import sys
import os
from typing import List, Tuple, Dict, Optional, Any
from dataclasses import dataclass
from enum import Enum

# Import GUI framework with fallbacks
try:
    from PySide2 import QtWidgets, QtCore, QtGui
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    QT_AVAILABLE = True
except ImportError:
    try:
        from PySide import QtWidgets, QtCore, QtGui
        from PySide.QtWidgets import *
        from PySide.QtCore import *
        from PySide.QtGui import *
        QT_AVAILABLE = True
    except ImportError:
        QT_AVAILABLE = False

# Import plotting library with fallback
try:
    import matplotlib
    matplotlib.use('Qt5Agg')  # Use Qt5Agg backend for FreeCAD
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.figure import Figure
    from mpl_toolkits.mplot3d import Axes3D
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

# Import the story forces module
try:
    from .story_forces import (
        calculate_seismic_coefficient, calculate_base_shear, 
        distribute_forces_asce, distribute_forces_linear, 
        distribute_forces_uniform, calculate_vertical_component,
        create_story_data_table, format_story_data_for_plot
    )
    STORY_FORCES_AVAILABLE = True
except ImportError:
    STORY_FORCES_AVAILABLE = False

class BuildingType(Enum):
    """Building type enumeration for different structural systems"""
    STEEL_MOMENT_FRAME = "Steel Moment Resisting Frame"
    CONCRETE_MOMENT_FRAME = "Concrete Moment Resisting Frame"
    STEEL_BRACED_FRAME = "Steel Braced Frame"
    CONCRETE_SHEAR_WALL = "Concrete Shear Wall"
    WOOD_FRAME = "Wood Frame"
    MASONRY_BEARING_WALL = "Masonry Bearing Wall"
    PRECAST_CONCRETE = "Precast Concrete"

class SeismicCode(Enum):
    """Seismic code enumeration"""
    ASCE_7_22 = "ASCE 7-22"
    TIS_1301_61 = "TIS 1301-61"
    IBC_2021 = "IBC 2021"
    EUROCODE_8 = "Eurocode 8"
    NBCC_2020 = "NBCC 2020"

# Building type specific parameters
BUILDING_TYPE_PARAMETERS = {
    BuildingType.STEEL_MOMENT_FRAME: {
        'ct': 0.028,  # Period coefficient
        'x': 0.8,     # Period exponent
        'r_factor': 8.0,  # Response modification factor
        'omega_factor': 2.5,  # Overstrength factor
        'cd_factor': 5.5,  # Deflection amplification factor
        'description': 'Steel moment-resisting frames with welded connections'
    },
    BuildingType.CONCRETE_MOMENT_FRAME: {
        'ct': 0.016,
        'x': 0.9,
        'r_factor': 8.0,
        'omega_factor': 2.5,
        'cd_factor': 5.5,
        'description': 'Reinforced concrete moment-resisting frames'
    },
    BuildingType.STEEL_BRACED_FRAME: {
        'ct': 0.030,
        'x': 0.75,
        'r_factor': 6.0,
        'omega_factor': 2.0,
        'cd_factor': 4.5,
        'description': 'Steel frames with concentric bracing'
    },
    BuildingType.CONCRETE_SHEAR_WALL: {
        'ct': 0.017,
        'x': 0.8,
        'r_factor': 5.0,
        'omega_factor': 2.5,
        'cd_factor': 4.0,
        'description': 'Reinforced concrete shear wall buildings'
    },
    BuildingType.WOOD_FRAME: {
        'ct': 0.035,
        'x': 0.75,
        'r_factor': 6.5,
        'omega_factor': 2.5,
        'cd_factor': 5.0,
        'description': 'Wood frame construction with shear walls'
    },
    BuildingType.MASONRY_BEARING_WALL: {
        'ct': 0.020,
        'x': 0.75,
        'r_factor': 2.5,
        'omega_factor': 2.5,
        'cd_factor': 2.5,
        'description': 'Unreinforced or reinforced masonry bearing wall buildings'
    },
    BuildingType.PRECAST_CONCRETE: {
        'ct': 0.020,
        'x': 0.75,
        'r_factor': 3.0,
        'omega_factor': 2.5,
        'cd_factor': 3.0,
        'description': 'Precast concrete structures with connections'
    }
}

# Site class parameters for different codes
SITE_CLASS_PARAMETERS = {
    SeismicCode.ASCE_7_22: {
        'A': {'description': 'Hard Rock', 'fa_min': 0.8, 'fa_max': 0.8, 'fv_min': 0.8, 'fv_max': 0.8},
        'B': {'description': 'Rock', 'fa_min': 0.9, 'fa_max': 0.9, 'fv_min': 0.9, 'fv_max': 0.9},
        'C': {'description': 'Very Dense Soil and Soft Rock', 'fa_min': 1.0, 'fa_max': 1.0, 'fv_min': 1.0, 'fv_max': 1.0},
        'D': {'description': 'Stiff Soil', 'fa_min': 1.2, 'fa_max': 1.2, 'fv_min': 1.5, 'fv_max': 1.5},
        'E': {'description': 'Soft Clay', 'fa_min': 1.5, 'fa_max': 1.5, 'fv_min': 2.0, 'fv_max': 2.0},
        'F': {'description': 'Site-Specific Analysis Required', 'fa_min': 1.0, 'fa_max': 1.0, 'fv_min': 1.0, 'fv_max': 1.0}
    },
    SeismicCode.TIS_1301_61: {
        'A': {'description': 'Rock', 'fa_min': 0.8, 'fa_max': 0.8, 'fv_min': 0.8, 'fv_max': 0.8},
        'B': {'description': 'Dense Soil', 'fa_min': 0.9, 'fa_max': 0.9, 'fv_min': 0.9, 'fv_max': 0.9},
        'C': {'description': 'Medium Soil', 'fa_min': 1.0, 'fa_max': 1.0, 'fv_min': 1.0, 'fv_max': 1.0},
        'D': {'description': 'Soft Soil', 'fa_min': 1.2, 'fa_max': 1.2, 'fv_min': 1.5, 'fv_max': 1.5},
        'E': {'description': 'Very Soft Soil', 'fa_min': 1.5, 'fa_max': 1.5, 'fv_min': 2.0, 'fv_max': 2.0}
    }
}

# Thai seismic zone parameters
THAI_SEISMIC_ZONES = {
    'Zone_A': {
        'description': 'Low seismicity zone (most of Thailand)',
        'ss_range': (0.1, 0.3),
        's1_range': (0.05, 0.15),
        'pga_range': (0.05, 0.15),
        'zone_factor': 0.1
    },
    'Zone_B': {
        'description': 'Moderate seismicity zone (border regions)',
        'ss_range': (0.3, 0.6),
        's1_range': (0.15, 0.3),
        'pga_range': (0.15, 0.3),
        'zone_factor': 0.2
    },
    'Zone_C': {
        'description': 'High seismicity zone (western border areas)',
        'ss_range': (0.6, 1.0),
        's1_range': (0.3, 0.6),
        'pga_range': (0.3, 0.6),
        'zone_factor': 0.4
    }
}

# Thai provinces with seismic considerations
THAI_PROVINCES = {
    "Bangkok": "Zone_A",
    "Samut Prakan": "Zone_A",
    "Nonthaburi": "Zone_A",
    "Pathum Thani": "Zone_A",
    "Phra Nakhon Si Ayutthaya": "Zone_A",
    "Chiang Mai": "Zone_B",
    "Chiang Rai": "Zone_B",
    "Lampang": "Zone_B",
    "Lamphun": "Zone_B",
    "Mae Hong Son": "Zone_B",
    "Nan": "Zone_B",
    "Phayao": "Zone_B",
    "Phrae": "Zone_B",
    "Uttaradit": "Zone_B",
    "Tak": "Zone_C",
    "Kamphaeng Phet": "Zone_C",
    "Nakhon Sawan": "Zone_B",
    "Phetchabun": "Zone_B",
    "Phitsanulok": "Zone_B",
    "Sukhothai": "Zone_B",
    "Uthai Thani": "Zone_B",
    "Kanchanaburi": "Zone_C",
    "Ratchaburi": "Zone_C",
    "Suphan Buri": "Zone_A",
    "Nakhon Pathom": "Zone_A",
    "Samut Sakhon": "Zone_A",
    "Samut Songkhram": "Zone_A"
}

@dataclass
class StaticSeismicParameters:
    """Static seismic analysis parameters"""
    # Basic parameters
    building_height: float = 30.0  # meters
    total_weight: float = 50000.0  # kN
    number_of_stories: int = 10
    
    # Seismic parameters
    sds: float = 1.0  # Design spectral response acceleration at short periods
    sd1: float = 0.4  # Design spectral response acceleration at 1-second period
    site_class: str = "C"  # Site class (A, B, C, D, E, F)
    risk_category: str = "II"  # Risk category (I, II, III, IV)
    
    # Structural parameters
    r_factor: float = 8.0  # Response modification factor
    omega_factor: float = 3.0  # Overstrength factor
    cd_factor: float = 5.5  # Deflection amplification factor
    importance_factor: float = 1.0  # Importance factor
    
    # Building type and code
    building_type: BuildingType = BuildingType.STEEL_MOMENT_FRAME
    seismic_code: SeismicCode = SeismicCode.ASCE_7_22
    
    # Thai specific parameters
    province: str = "Bangkok"
    seismic_zone: str = "Zone_A"
    
    # Story data
    story_heights: List[float] = None
    story_weights: List[float] = None
    
    # Analysis options
    distribution_method: str = "ASCE 7-22"  # ASCE 7-22, Linear, Uniform, Custom
    include_vertical: bool = False
    vertical_factor: float = 0.2  # Default ASCE 7-22 value
    
    def __post_init__(self):
        if self.story_heights is None:
            # Default story heights (uniform)
            story_height = self.building_height / self.number_of_stories
            self.story_heights = [(i + 1) * story_height for i in range(self.number_of_stories)]
        if self.story_weights is None:
            # Default story weights (uniform)
            self.story_weights = [self.total_weight / self.number_of_stories] * self.number_of_stories

class StaticSeismicAnalyzer:
    """Static seismic analyzer for calculating story forces distribution"""
    
    def __init__(self, parameters: StaticSeismicParameters = None):
        self.parameters = parameters or StaticSeismicParameters()
        self.results = None
        self.story_forces = None
        self.base_shear = None
        self.vertical_force = None
        self.period = None
    
    def calculate_fundamental_period(self) -> float:
        """Calculate approximate fundamental period per seismic code"""
        # Get building type parameters
        building_type_params = BUILDING_TYPE_PARAMETERS.get(self.parameters.building_type, 
                                                          BUILDING_TYPE_PARAMETERS[BuildingType.STEEL_MOMENT_FRAME])
        
        ct = building_type_params['ct']
        x = building_type_params['x']
        
        # Calculate period based on seismic code
        if self.parameters.seismic_code == SeismicCode.ASCE_7_22:
            return ct * (self.parameters.building_height ** x)
        elif self.parameters.seismic_code == SeismicCode.TIS_1301_61:
            # TIS 1301-61 formula
            return 0.085 * (self.parameters.building_height ** 0.75)
        else:
            # Default to ASCE 7-22
            return ct * (self.parameters.building_height ** x)
    
    def calculate_seismic_coefficient(self) -> float:
        """Calculate seismic response coefficient"""
        if not STORY_FORCES_AVAILABLE:
            # Fallback calculation
            return 0.1  # Default value
        
        period = self.calculate_fundamental_period()
        return calculate_seismic_coefficient(
            self.parameters.sds, self.parameters.sd1, period,
            self.parameters.r_factor, self.parameters.importance_factor
        )
    
    def calculate_base_shear(self) -> float:
        """Calculate seismic base shear"""
        cs = self.calculate_seismic_coefficient()
        if STORY_FORCES_AVAILABLE:
            return calculate_base_shear(self.parameters.total_weight, cs)
        else:
            return self.parameters.total_weight * cs
    
    def calculate_story_forces(self) -> List[float]:
        """Calculate story forces distribution"""
        base_shear = self.calculate_base_shear()
        period = self.calculate_fundamental_period()
        
        if not STORY_FORCES_AVAILABLE:
            # Fallback uniform distribution
            return [base_shear / self.parameters.number_of_stories] * self.parameters.number_of_stories
        
        # Select distribution method
        if self.parameters.distribution_method == "ASCE 7-22":
            return distribute_forces_asce(
                base_shear, self.parameters.story_heights, 
                self.parameters.story_weights, period
            )
        elif self.parameters.distribution_method == "Linear":
            return distribute_forces_linear(base_shear, self.parameters.story_heights)
        elif self.parameters.distribution_method == "Uniform":
            return distribute_forces_uniform(base_shear, self.parameters.number_of_stories)
        else:  # Custom
            # For custom, we'll use uniform as fallback
            return distribute_forces_uniform(base_shear, self.parameters.number_of_stories)
    
    def calculate_vertical_force(self) -> float:
        """Calculate vertical seismic component"""
        base_shear = self.calculate_base_shear()
        if STORY_FORCES_AVAILABLE and self.parameters.include_vertical:
            # Different codes may have different vertical force calculations
            if self.parameters.seismic_code == SeismicCode.TIS_1301_61:
                # TIS 1301-61 might use a different factor
                return calculate_vertical_component(base_shear, self.parameters.sds, 0.2)
            else:
                # Default ASCE 7-22 method
                return calculate_vertical_component(
                    base_shear, self.parameters.sds, self.parameters.vertical_factor
                )
        return 0.0
    
    def get_code_specific_parameters(self) -> Dict[str, Any]:
        """Get code-specific parameters for the selected seismic code"""
        params = {}
        
        if self.parameters.seismic_code == SeismicCode.ASCE_7_22:
            # ASCE 7-22 specific parameters
            params['code_name'] = "ASCE 7-22"
            params['version'] = "2022"
            params['vertical_force_factor'] = 0.2  # 0.2*SDS
            params['minimum_base_shear_factor'] = 0.044  # 0.044*SDS*Ie
        elif self.parameters.seismic_code == SeismicCode.TIS_1301_61:
            # TIS 1301-61 specific parameters
            params['code_name'] = "TIS 1301-61"
            params['version'] = "2021"
            params['vertical_force_factor'] = 0.2  # Same as ASCE for now
            params['minimum_base_shear_factor'] = 0.044  # Same as ASCE for now
            # Add Thai-specific parameters
            zone_info = THAI_SEISMIC_ZONES.get(self.parameters.seismic_zone, THAI_SEISMIC_ZONES["Zone_A"])
            params['zone_description'] = zone_info['description']
            params['zone_factor'] = zone_info['zone_factor']
        else:
            # Default to ASCE 7-22
            params['code_name'] = "ASCE 7-22"
            params['version'] = "2022"
            params['vertical_force_factor'] = 0.2
            params['minimum_base_shear_factor'] = 0.044
        
        return params
    
    def get_thai_seismic_zone(self) -> str:
        """Get Thai seismic zone based on province"""
        return THAI_PROVINCES.get(self.parameters.province, "Zone_A")
    
    def get_building_type_description(self) -> str:
        """Get description of the selected building type"""
        building_type_params = BUILDING_TYPE_PARAMETERS.get(self.parameters.building_type)
        if building_type_params:
            return building_type_params.get('description', 'Unknown building type')
        return 'Unknown building type'
    
    def perform_analysis(self) -> Dict[str, Any]:
        """Perform complete static seismic analysis"""
        # Calculate key parameters
        self.period = self.calculate_fundamental_period()
        self.base_shear = self.calculate_base_shear()
        self.story_forces = self.calculate_story_forces()
        self.vertical_force = self.calculate_vertical_force()
        
        # Get code-specific parameters
        code_params = self.get_code_specific_parameters()
        
        # Get Thai seismic zone if using Thai code
        thai_zone = None
        if self.parameters.seismic_code == SeismicCode.TIS_1301_61:
            thai_zone = self.get_thai_seismic_zone()
        
        # Create results dictionary
        self.results = {
            'period': self.period,
            'base_shear': self.base_shear,
            'story_forces': self.story_forces,
            'vertical_force': self.vertical_force,
            'story_heights': self.parameters.story_heights,
            'story_weights': self.parameters.story_weights,
            'code_parameters': code_params,
            'building_type_description': self.get_building_type_description(),
            'thai_seismic_zone': thai_zone
        }
        
        return self.results
    
    def get_story_data_table(self) -> List[Dict[str, Any]]:
        """Get story data in table format for display"""
        if not STORY_FORCES_AVAILABLE or self.story_forces is None:
            return []
        
        return create_story_data_table(
            self.story_forces, self.parameters.story_heights, self.parameters.story_weights
        )

def plot_3d_load_pattern(story_forces: List[float], story_heights: List[float], 
                        building_width: float = 20.0, building_length: float = 40.0,
                        direction: str = 'X'):
    """
    Create a 3D visualization of the load pattern applied to a building structure.
    
    Args:
        story_forces: List of story forces (kN)
        story_heights: List of story heights from ground (m)
        building_width: Width of the building (m)
        building_length: Length of the building (m)
        direction: Load direction ('X' or 'Y')
    """
    if not MATPLOTLIB_AVAILABLE:
        return None
    
    try:
        # Create figure and 3D axis
        fig = Figure(figsize=(10, 8), dpi=100)
        ax = fig.add_subplot(111, projection='3d')
        
        # Building dimensions
        width = building_width
        length = building_length
        heights = story_heights
        
        # Create building frame (simplified as a rectangular prism)
        x = [0, width, width, 0, 0]
        y = [0, 0, length, length, 0]
        z_base = [0, 0, 0, 0, 0]
        
        # Plot building base
        for i in range(len(x)-1):
            ax.plot([x[i], x[i+1]], [y[i], y[i+1]], [z_base[i], z_base[i]], 'k-', linewidth=1)
        
        # Plot building corners vertically
        for i in range(4):
            ax.plot([x[i], x[i]], [y[i], y[i]], [0, heights[-1]], 'k-', linewidth=1)
        
        # Plot floor slabs
        for height in heights:
            ax.plot(x, y, [height, height, height, height, height], 'k--', linewidth=0.5, alpha=0.5)
        
        # Plot load vectors
        max_force = max(story_forces) if story_forces else 1.0
        scale_factor = 10.0 / max_force if max_force > 0 else 1.0
        
        center_x = width / 2
        center_y = length / 2
        
        for i, (force, height) in enumerate(zip(story_forces, heights)):
            # Scale the force for visualization
            scaled_force = force * scale_factor
            
            # Determine load direction
            if direction.upper() == 'X':
                # Load in X direction (left/right)
                start_x, start_y = center_x, center_y
                end_x, end_y = center_x + scaled_force, center_y
            else:  # Y direction
                # Load in Y direction (forward/backward)
                start_x, start_y = center_x, center_y
                end_x, end_y = center_x, center_y + scaled_force
            
            # Draw force vector
            ax.quiver(start_x, start_y, height, 
                     end_x - start_x, end_y - start_y, 0,
                     color='red', arrow_length_ratio=0.1, linewidth=2)
            
            # Add force magnitude label
            ax.text(end_x, end_y, height, f'{force:.1f} kN', 
                   color='red', fontsize=8, ha='center', va='bottom')
        
        # Set labels and title
        ax.set_xlabel('Width (m)')
        ax.set_ylabel('Length (m)')
        ax.set_zlabel('Height (m)')
        ax.set_title(f'3D Load Pattern Visualization - {direction} Direction')
        
        # Set axis limits
        ax.set_xlim(0, width * 1.5)
        ax.set_ylim(0, length * 1.5)
        ax.set_zlim(0, heights[-1] * 1.2 if heights else 10)
        
        return fig
        
    except Exception as e:
        print(f"Error creating 3D load pattern visualization: {e}")
        return None

def create_static_seismic_tab(parent=None):
    """Create Static Seismic tab with professional MIDAS nGen-like interface"""
    if not QT_AVAILABLE:
        return None
    
    widget = QWidget()
    layout = QGridLayout()
    
    # Title Header
    title_label = QLabel("Static Seismic Load")
    title_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #C2185B; padding: 5px;")
    title_label.setAlignment(Qt.AlignCenter)
    layout.addWidget(title_label, 0, 0, 1, 2)
    
    # Seismic Code Selection
    code_group = QGroupBox("Seismic Code")
    code_layout = QGridLayout()
    
    code_layout.addWidget(QLabel("Design Code:"), 0, 0)
    static_code_combo = QComboBox()
    static_code_combo.addItems(["ASCE 7-22", "TIS 1301-61", "Custom"])
    code_layout.addWidget(static_code_combo, 0, 1)
    
    code_group.setLayout(code_layout)
    layout.addWidget(code_group, 1, 0, 1, 2)
    
    # Site Class and Risk Category
    site_group = QGroupBox("Site and Building Characteristics")
    site_layout = QGridLayout()
    
    site_layout.addWidget(QLabel("Site Class:"), 0, 0)
    static_site_class_combo = QComboBox()
    static_site_class_combo.addItems(["A", "B", "C", "D", "E", "F"])
    static_site_class_combo.setCurrentText("C")
    site_layout.addWidget(static_site_class_combo, 0, 1)
    
    site_layout.addWidget(QLabel("Risk Category:"), 1, 0)
    risk_category_combo = QComboBox()
    risk_category_combo.addItems(["I", "II", "III", "IV"])
    site_layout.addWidget(risk_category_combo, 1, 1)
    
    site_group.setLayout(site_layout)
    layout.addWidget(site_group, 2, 0, 1, 2)
    
    # Response Parameters
    response_group = QGroupBox("Response Parameters")
    response_layout = QGridLayout()
    
    response_layout.addWidget(QLabel("Response Modification (R):"), 0, 0)
    r_factor_edit = QLineEdit("8.0")
    response_layout.addWidget(r_factor_edit, 0, 1)
    
    response_layout.addWidget(QLabel("Overstrength Factor (Ω₀):"), 1, 0)
    omega_factor_edit = QLineEdit("3.0")
    response_layout.addWidget(omega_factor_edit, 1, 1)
    
    response_layout.addWidget(QLabel("Deflection Amplification (Cd):"), 2, 0)
    cd_factor_edit = QLineEdit("5.5")
    response_layout.addWidget(cd_factor_edit, 2, 1)
    
    response_layout.addWidget(QLabel("Importance Factor (Ie):"), 3, 0)
    ie_factor_edit = QLineEdit("1.0")
    response_layout.addWidget(ie_factor_edit, 3, 1)
    
    response_group.setLayout(response_layout)
    layout.addWidget(response_group, 3, 0, 1, 2)
    
    # Seismic Coefficients
    coeff_group = QGroupBox("Seismic Coefficients")
    coeff_layout = QGridLayout()
    
    coeff_layout.addWidget(QLabel("SS (Mapped short period):"), 0, 0)
    ss_static_edit = QLineEdit("1.5")
    coeff_layout.addWidget(ss_static_edit, 0, 1)
    
    coeff_layout.addWidget(QLabel("S1 (Mapped 1-second period):"), 1, 0)
    s1_static_edit = QLineEdit("0.6")
    coeff_layout.addWidget(s1_static_edit, 1, 1)
    
    coeff_layout.addWidget(QLabel("SDS (Design short period):"), 2, 0)
    sds_static_edit = QLineEdit("1.0")
    coeff_layout.addWidget(sds_static_edit, 2, 1)
    
    coeff_layout.addWidget(QLabel("SD1 (Design 1-second):"), 3, 0)
    sd1_static_edit = QLineEdit("0.4")
    coeff_layout.addWidget(sd1_static_edit, 3, 1)
    
    coeff_group.setLayout(coeff_layout)
    layout.addWidget(coeff_group, 4, 0, 1, 2)
    
    # Story Forces Distribution
    story_group = QGroupBox("Story Forces Distribution")
    story_layout = QVBoxLayout()
    
    # Distribution Method
    dist_layout = QHBoxLayout()
    dist_layout.addWidget(QLabel("Distribution Method:"))
    dist_method_combo = QComboBox()
    dist_method_combo.addItems(["ASCE 7-22", "Linear", "Uniform", "Custom"])
    dist_layout.addWidget(dist_method_combo)
    story_layout.addLayout(dist_layout)
    
    # Story Data Table
    story_table = QTableWidget(10, 4)
    story_table.setHorizontalHeaderLabels(["Story", "Height (m)", "Weight (kN)", "Force (kN)"])
    story_table.setColumnWidth(0, 60)
    story_table.setColumnWidth(1, 100)
    story_table.setColumnWidth(2, 100)
    story_table.setColumnWidth(3, 100)
    
    # Populate with sample data
    for i in range(10):
        story_num = 10 - i
        height = (i + 1) * 3.0
        weight = 5000.0
        story_table.setItem(i, 0, QTableWidgetItem(str(story_num)))
        story_table.setItem(i, 1, QTableWidgetItem(f"{height:.1f}"))
        story_table.setItem(i, 2, QTableWidgetItem(f"{weight:.1f}"))
        story_table.setItem(i, 3, QTableWidgetItem(""))
    
    story_layout.addWidget(story_table)
    
    # Story Forces Visualization
    if MATPLOTLIB_AVAILABLE:
        try:
            story_figure = Figure(figsize=(5, 3), dpi=100)
            story_canvas = FigureCanvas(story_figure)
            story_axes = story_figure.add_subplot(111)
            story_axes.set_xlabel('Story Force (kN)')
            story_axes.set_ylabel('Height (m)')
            story_axes.grid(True, linestyle='--', alpha=0.7)
            story_layout.addWidget(story_canvas)
        except Exception as e:
            fallback_label = QLabel("Plot not available: matplotlib error")
            story_layout.addWidget(fallback_label)
    else:
        fallback_label = QLabel("Plot not available: matplotlib required")
        story_layout.addWidget(fallback_label)
    
    story_group.setLayout(story_layout)
    layout.addWidget(story_group, 5, 0, 1, 2)
    
    # Vertical Component
    vertical_group = QGroupBox("Vertical Component")
    vertical_layout = QHBoxLayout()
    
    vertical_check = QCheckBox("Include Vertical Seismic Component")
    vertical_check.setChecked(False)
    vertical_layout.addWidget(vertical_check)
    
    vertical_group.setLayout(vertical_layout)
    layout.addWidget(vertical_group, 6, 0, 1, 2)
    
    # Base Shear Results
    results_group = QGroupBox("Base Shear Results")
    results_layout = QGridLayout()
    
    results_layout.addWidget(QLabel("Base Shear X:"), 0, 0)
    base_shear_x_label = QLabel("0.0 kN")
    results_layout.addWidget(base_shear_x_label, 0, 1)
    
    results_layout.addWidget(QLabel("Base Shear Y:"), 1, 0)
    base_shear_y_label = QLabel("0.0 kN")
    results_layout.addWidget(base_shear_y_label, 1, 1)
    
    results_layout.addWidget(QLabel("Total Weight:"), 2, 0)
    total_weight_label = QLabel("50000.0 kN")
    results_layout.addWidget(total_weight_label, 2, 1)
    
    results_group.setLayout(results_layout)
    layout.addWidget(results_group, 7, 0, 1, 2)
    
    widget.setLayout(layout)
    return widget

# Example usage
if __name__ == "__main__":
    # Create sample parameters
    params = StaticSeismicParameters(
        building_height=30.0,
        total_weight=50000.0,
        number_of_stories=10,
        sds=1.0,
        sd1=0.4,
        r_factor=8.0,
        importance_factor=1.0
    )
    
    # Create analyzer
    analyzer = StaticSeismicAnalyzer(params)
    
    # Perform analysis
    results = analyzer.perform_analysis()
    
    # Print results
    print("Static Seismic Analysis Results")
    print("=" * 40)
    print(f"Building Height: {params.building_height} m")
    print(f"Number of Stories: {params.number_of_stories}")
    print(f"Total Weight: {params.total_weight} kN")
    print(f"Fundamental Period: {results['period']:.3f} sec")
    print(f"Base Shear: {results['base_shear']:.1f} kN")
    print(f"Vertical Force: {results['vertical_force']:.1f} kN")
    print(f"Building Type: {results['building_type_description']}")
    print(f"Code: {results['code_parameters']['code_name']} {results['code_parameters']['version']}")
    if results['thai_seismic_zone']:
        print(f"Thai Seismic Zone: {results['thai_seismic_zone']}")
    print("\nStory Forces Distribution:")
    
    # Get story data table
    story_data = analyzer.get_story_data_table()
    for row in story_data:
        print(f"Story {row['story']}: {row['height']:.1f}m, {row['weight']:.1f}kN, {row['force']:.1f}kN ({row['percentage']:.1f}%)")
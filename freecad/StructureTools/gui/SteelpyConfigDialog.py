# -*- coding: utf-8 -*-
"""
Steelpy Configuration Dialog

Dialog for configuring steelpy database directory and settings.
"""

import os
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QFormLayout, 
                               QLineEdit, QPushButton, QLabel, QGroupBox, 
                               QCheckBox, QFileDialog, QMessageBox, QListWidget,
                               QProgressBar, QTextEdit)
from PySide2.QtCore import Qt, QThread, QTimer
from PySide2.QtGui import QFont

try:
    import FreeCAD as App
except ImportError:
    App = None


class SteelpyConfigDialog(QDialog):
    """Configuration dialog for steelpy database integration"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Configure Steelpy Database")
        self.setModal(True)
        self.resize(600, 500)
        
        # Current configuration
        self.steelpy_directory = None
        self.available_databases = {}
        
        self.setup_ui()
        self.load_current_config()
    
    def setup_ui(self):
        """Create the user interface"""
        layout = QVBoxLayout(self)
        
        # Header
        header_label = QLabel("Steelpy Database Configuration")
        header_font = QFont()
        header_font.setPointSize(14)
        header_font.setBold(True)
        header_label.setFont(header_font)
        header_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(header_label)
        
        # Description
        desc_text = """
Steelpy provides comprehensive AISC steel section databases including W-shapes, 
HSS, Pipes, Channels, Angles, and more. Configure the path to steelpy shape files 
to enable thousands of standard steel sections in your structural profiles.
        """
        desc_label = QLabel(desc_text)
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("color: #666; margin: 10px;")
        layout.addWidget(desc_label)
        
        # Directory Configuration
        dir_group = QGroupBox("Database Directory")
        dir_layout = QFormLayout(dir_group)
        
        # Directory selection
        dir_select_layout = QHBoxLayout()
        self.directory_edit = QLineEdit()
        self.directory_edit.setPlaceholderText("Select steelpy shape files directory...")
        self.directory_edit.textChanged.connect(self.on_directory_changed)
        
        self.browse_btn = QPushButton("📁 Browse")
        self.browse_btn.clicked.connect(self.browse_directory)
        
        dir_select_layout.addWidget(self.directory_edit, 1)
        dir_select_layout.addWidget(self.browse_btn)
        dir_layout.addRow("Steelpy Directory:", dir_select_layout)
        
        # Auto-detect button
        self.autodetect_btn = QPushButton("🔍 Auto-detect Steelpy Installation")
        self.autodetect_btn.clicked.connect(self.auto_detect_steelpy)
        dir_layout.addRow(self.autodetect_btn)
        
        layout.addWidget(dir_group)
        
        # Database Status
        status_group = QGroupBox("Database Status")
        status_layout = QVBoxLayout(status_group)
        
        self.status_label = QLabel("No directory selected")
        self.status_label.setStyleSheet("color: #666;")
        status_layout.addWidget(self.status_label)
        
        # Available databases list
        self.databases_list = QListWidget()
        self.databases_list.setMaximumHeight(150)
        status_layout.addWidget(QLabel("Available Databases:"))
        status_layout.addWidget(self.databases_list)
        
        # Progress bar for loading
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        status_layout.addWidget(self.progress_bar)
        
        layout.addWidget(status_group)
        
        # Download/Install Section
        install_group = QGroupBox("Installation Help")
        install_layout = QVBoxLayout(install_group)
        
        install_text = QTextEdit()
        install_text.setMaximumHeight(120)
        install_text.setReadOnly(True)
        install_text.setHtml('''
        <h4>How to get steelpy shape files:</h4>
        <ol>
            <li><b>Download:</b> Visit <a href="https://github.com/steelpy/steelpy">github.com/steelpy/steelpy</a></li>
            <li><b>Extract:</b> Download or clone the repository</li>
            <li><b>Locate:</b> Find the "steelpy/shape files" directory</li>
            <li><b>Configure:</b> Point to this directory in the field above</li>
        </ol>
        ''')
        install_layout.addWidget(install_text)
        
        self.download_btn = QPushButton("🌐 Open Steelpy GitHub")
        self.download_btn.clicked.connect(self.open_steelpy_github)
        install_layout.addWidget(self.download_btn)
        
        layout.addWidget(install_group)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        self.test_btn = QPushButton("🧪 Test Configuration")
        self.test_btn.clicked.connect(self.test_configuration)
        self.test_btn.setEnabled(False)
        
        self.apply_btn = QPushButton("✅ Apply Configuration")
        self.apply_btn.clicked.connect(self.apply_configuration)
        self.apply_btn.setEnabled(False)
        
        self.cancel_btn = QPushButton("❌ Cancel")
        self.cancel_btn.clicked.connect(self.reject)
        
        button_layout.addWidget(self.test_btn)
        button_layout.addWidget(self.apply_btn)
        button_layout.addStretch()
        button_layout.addWidget(self.cancel_btn)
        
        layout.addLayout(button_layout)
    
    def load_current_config(self):
        """Load current steelpy configuration"""
        try:
            from ..data.SteelpyDatabaseIntegration import steelpy_manager, is_steelpy_available
            
            if is_steelpy_available() and steelpy_manager:
                current_dir = steelpy_manager.shape_directory
                if current_dir and os.path.exists(current_dir):
                    self.directory_edit.setText(current_dir)
                    self.validate_directory(current_dir)
        except ImportError:
            pass
    
    def browse_directory(self):
        """Open directory browser"""
        directory = QFileDialog.getExistingDirectory(
            self, 
            "Select Steelpy Shape Files Directory",
            os.path.expanduser("~"),
            QFileDialog.ShowDirsOnly
        )
        
        if directory:
            self.directory_edit.setText(directory)
    
    def on_directory_changed(self):
        """Handle directory path change"""
        directory = self.directory_edit.text().strip()
        if directory and os.path.exists(directory):
            self.validate_directory(directory)
        else:
            self.reset_status()
    
    def validate_directory(self, directory):
        """Validate steelpy directory and show available databases"""
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)  # Indeterminate progress
        
        # Use timer to allow UI to update
        QTimer.singleShot(100, lambda: self._do_validation(directory))
    
    def _do_validation(self, directory):
        """Perform actual validation"""
        try:
            from ..data.SteelpyDatabaseIntegration import SteelpyDatabaseManager
            
            # Create temporary manager to test
            temp_manager = SteelpyDatabaseManager(directory)
            
            # Check for CSV files
            expected_files = [
                "W_shapes.csv", "HSS_shapes.csv", "PIPE_shapes.csv", 
                "L_shapes.csv", "C_shapes.csv", "MC_shapes.csv"
            ]
            
            found_files = []
            self.available_databases = {}
            
            for filename in expected_files:
                filepath = os.path.join(directory, filename)
                if os.path.exists(filepath):
                    found_files.append(filename)
                    
                    # Try to get profile count
                    kind = filename.split('_')[0]
                    try:
                        profiles = temp_manager.get_available_profiles(kind)
                        self.available_databases[kind] = len(profiles)
                    except:
                        self.available_databases[kind] = "Unknown"
            
            if found_files:
                self.status_label.setText(f"✅ Valid steelpy directory - {len(found_files)} databases found")
                self.status_label.setStyleSheet("color: green; font-weight: bold;")
                
                # Update databases list
                self.databases_list.clear()
                for kind, count in self.available_databases.items():
                    item_text = f"{kind}_shapes.csv ({count} profiles)" if count != "Unknown" else f"{kind}_shapes.csv"
                    self.databases_list.addItem(item_text)
                
                self.steelpy_directory = directory
                self.test_btn.setEnabled(True)
                self.apply_btn.setEnabled(True)
                
            else:
                self.status_label.setText("❌ No steelpy CSV files found in directory")
                self.status_label.setStyleSheet("color: red;")
                self.reset_status()
                
        except Exception as e:
            self.status_label.setText(f"❌ Error validating directory: {str(e)}")
            self.status_label.setStyleSheet("color: red;")
            self.reset_status()
        
        finally:
            self.progress_bar.setVisible(False)
    
    def reset_status(self):
        """Reset status to default"""
        self.databases_list.clear()
        self.available_databases = {}
        self.steelpy_directory = None
        self.test_btn.setEnabled(False)
        self.apply_btn.setEnabled(False)
    
    def auto_detect_steelpy(self):
        """Auto-detect steelpy installation"""
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)
        
        # Common locations to check
        search_paths = [
            os.path.expanduser("~/steelpy/steelpy/shape files"),
            os.path.expanduser("~/Downloads/steelpy-main/steelpy/shape files"),
            os.path.expanduser("~/Documents/steelpy/steelpy/shape files"),
            "C:/steelpy/steelpy/shape files",
            "D:/steelpy/steelpy/shape files",
        ]
        
        # Check Python site-packages
        try:
            import site
            for site_dir in site.getsitepackages():
                search_paths.append(os.path.join(site_dir, "steelpy", "shape files"))
        except:
            pass
        
        found_path = None
        for path in search_paths:
            if os.path.exists(path):
                # Check if it contains CSV files
                csv_files = [f for f in os.listdir(path) if f.endswith('_shapes.csv')]
                if csv_files:
                    found_path = path
                    break
        
        self.progress_bar.setVisible(False)
        
        if found_path:
            self.directory_edit.setText(found_path)
            QMessageBox.information(self, "Auto-detect Success", 
                                  f"Found steelpy installation at:\n{found_path}")
        else:
            QMessageBox.information(self, "Auto-detect Result", 
                                  "Could not auto-detect steelpy installation.\nPlease browse manually or install steelpy first.")
    
    def test_configuration(self):
        """Test the steelpy configuration"""
        if not self.steelpy_directory:
            return
        
        try:
            from ..data.SteelpyDatabaseIntegration import SteelpyDatabaseManager, SteelpyGeometryGenerator
            
            # Create test manager
            test_manager = SteelpyDatabaseManager(self.steelpy_directory)
            test_generator = SteelpyGeometryGenerator(test_manager)
            
            # Try to load a sample profile
            test_cases = [
                ("W", "W12X26"),
                ("HSS", "HSS6X4X3/8"), 
                ("L", "L4X3X1/2"),
                ("PIPE", "PIPE 4 SCH 40")
            ]
            
            results = []
            for kind, designation in test_cases:
                try:
                    properties = test_manager.get_profile_properties(kind, designation)
                    if properties:
                        results.append(f"✅ {kind}: {designation} - OK")
                    else:
                        results.append(f"❌ {kind}: {designation} - Not found")
                except:
                    results.append(f"❌ {kind}: {designation} - Error")
            
            result_text = "\n".join(results)
            QMessageBox.information(self, "Test Results", f"Configuration Test Results:\n\n{result_text}")
            
        except Exception as e:
            QMessageBox.critical(self, "Test Failed", f"Configuration test failed:\n{str(e)}")
    
    def apply_configuration(self):
        """Apply the steelpy configuration"""
        if not self.steelpy_directory:
            return
        
        try:
            from ..data.SteelpyDatabaseIntegration import configure_steelpy_integration
            
            # Configure steelpy integration
            configure_steelpy_integration(self.steelpy_directory)
            
            QMessageBox.information(self, "Configuration Applied", 
                                  f"Steelpy integration configured successfully!\n\n"
                                  f"Directory: {self.steelpy_directory}\n"
                                  f"Databases: {len(self.available_databases)}")
            
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(self, "Configuration Failed", 
                               f"Failed to apply configuration:\n{str(e)}")
    
    def open_steelpy_github(self):
        """Open steelpy GitHub page"""
        import webbrowser
        webbrowser.open("https://github.com/steelpy/steelpy")


def show_steelpy_config_dialog(parent=None):
    """Show steelpy configuration dialog"""
    dialog = SteelpyConfigDialog(parent)
    return dialog.exec_()
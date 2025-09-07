# -*- coding: utf-8 -*-
"""
Quick Section Manager - รวมทุกวิธีเปิด Advanced Section Manager
แก้ปัญหา GUI เด้งหายไป
"""

import FreeCAD as App

def method1_taskpanel():
    """วิธีที่ 1: เปิดแบบ TaskPanel (แนะนำ - เสถียรที่สุด)"""
    print("=" * 50)
    print("วิธีที่ 1: TaskPanel Version (เสถียรที่สุด)")
    print("=" * 50)
    
    try:
        from freecad.StructureTools.gui.SectionManagerTaskPanel import show_advanced_section_manager_task_panel
        
        result = show_advanced_section_manager_task_panel()
        
        if result:
            print("✅ สำเร็จ! TaskPanel เปิดแล้ว")
            print("📍 ดู TaskPanel ที่ด้านขว้าของ FreeCAD")
            return True
        else:
            print("❌ TaskPanel เปิดไม่ได้")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def method2_command():
    """วิธีที่ 2: ใช้ FreeCAD Command"""
    print("\n" + "=" * 50)
    print("วิธีที่ 2: FreeCAD Command")
    print("=" * 50)
    
    try:
        import FreeCADGui as Gui
        
        # ลอง TaskPanel command ก่อน
        print("🔄 ลองเปิด TaskPanel Command...")
        try:
            Gui.runCommand('StructureTools_AdvancedSectionManagerTaskPanel')
            print("✅ TaskPanel Command สำเร็จ!")
            return True
        except:
            print("⚠️ TaskPanel Command ไม่ได้")
        
        # ลอง GUI command
        print("🔄 ลองเปิด GUI Command...")
        try:
            Gui.runCommand('StructureTools_AdvancedSectionManager')
            print("✅ GUI Command สำเร็จ!")
            return True
        except:
            print("❌ GUI Command ไม่ได้")
        
        return False
        
    except Exception as e:
        print(f"❌ Command Error: {e}")
        return False

def method3_direct_gui():
    """วิธีที่ 3: เปิด GUI โดยตรง (อาจเด้งหายไป)"""
    print("\n" + "=" * 50)
    print("วิธีที่ 3: Direct GUI (อาจไม่เสถียร)")
    print("=" * 50)
    
    try:
        from freecad.StructureTools.gui.SectionManagerGUI import show_section_manager_gui
        
        print("🔄 เปิด GUI โดยตรง...")
        gui = show_section_manager_gui()
        
        if gui:
            print("✅ GUI เปิดแล้ว (แต่อาจหายไป)")
            print("📍 ถ้าหายไป ให้ลองวิธีอื่น")
            return True
        else:
            print("❌ GUI เปิดไม่ได้")
            return False
            
    except Exception as e:
        print(f"❌ GUI Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def method4_simple_dialog():
    """วิธีที่ 4: Simple Dialog สำรอง"""
    print("\n" + "=" * 50)
    print("วิธีที่ 4: Simple Dialog (สำรอง)")
    print("=" * 50)
    
    try:
        from freecad.StructureTools.gui.SectionManagerTaskPanel import AdvancedSectionManagerTaskPanel
        
        # ลองสร้าง TaskPanel แบบง่าย
        print("🔄 สร้าง Simple TaskPanel...")
        panel = AdvancedSectionManagerTaskPanel()
        
        if panel and hasattr(panel, 'form'):
            print("✅ Simple TaskPanel สร้างได้")
            
            # แสดงแบบ Dialog ธรรมดา
            try:
                from PySide2.QtWidgets import QDialog, QVBoxLayout, QPushButton
            except:
                from PySide.QtWidgets import QDialog, QVBoxLayout, QPushButton
            
            dialog = QDialog()
            dialog.setWindowTitle("Advanced Section Manager - Simple Version")
            dialog.setGeometry(200, 200, 800, 600)
            
            layout = QVBoxLayout(dialog)
            layout.addWidget(panel.form)
            
            close_btn = QPushButton("Close")
            close_btn.clicked.connect(dialog.close)
            layout.addWidget(close_btn)
            
            dialog.show()
            dialog.raise_()
            dialog.activateWindow()
            
            # เก็บ reference
            if not hasattr(method4_simple_dialog, '_dialogs'):
                method4_simple_dialog._dialogs = []
            method4_simple_dialog._dialogs.append(dialog)
            
            print("✅ Simple Dialog เปิดแล้ว!")
            return True
        else:
            print("❌ Simple TaskPanel สร้างไม่ได้")
            return False
            
    except Exception as e:
        print(f"❌ Simple Dialog Error: {e}")
        return False

def run_quick_section_manager():
    """รันทุกวิธี จนกว่าจะได้อันใดอันหนึ่ง"""
    print("🚀 Advanced Section Manager - Quick Launcher")
    print("🎯 จะลองทุกวิธีจนกว่าจะเปิดได้")
    print("=" * 60)
    
    methods = [
        ("TaskPanel (แนะนำ)", method1_taskpanel),
        ("Command", method2_command),
        ("Direct GUI", method3_direct_gui),
        ("Simple Dialog", method4_simple_dialog)
    ]
    
    for method_name, method_func in methods:
        print(f"\n🔧 ลอง {method_name}...")
        try:
            success = method_func()
            if success:
                print(f"\n🎉 สำเร็จแล้ว! ใช้วิธี: {method_name}")
                print("\n📋 วิธีใช้:")
                print("1. เลือก Shape Type (เช่น Wide Flange Beams)")
                print("2. เลือก Section จากรายการ")
                print("3. ดู Properties ที่แสดง")
                print("4. คลิก 'Create StructureTools Section' เพื่อสร้าง")
                print("\n⚡ หากยังไม่เห็น steelpy sections:")
                print("   pip install steelpy")
                print("   แล้วเปิด FreeCAD ใหม่")
                return True
                
        except Exception as e:
            print(f"❌ {method_name} failed: {e}")
    
    print("\n😞 เปิดไม่ได้ทุกวิธี - ลองตรวจสอบ:")
    print("1. pip install PySide2")
    print("2. pip install steelpy")  
    print("3. เปิด FreeCAD ใหม่")
    print("4. ลองรันสคริปต์นี้อีกครั้ง")
    
    return False

def show_debug_info():
    """แสดงข้อมูลการ debug"""
    print("\n" + "=" * 60)
    print("🔍 DEBUG INFORMATION")
    print("=" * 60)
    
    # Check PySide
    try:
        from PySide2 import QtWidgets
        print("✅ PySide2 available")
    except:
        try:
            from PySide import QtWidgets  
            print("✅ PySide available")
        except:
            print("❌ No PySide available - install PySide2")
    
    # Check steelpy
    try:
        from freecad.StructureTools.data.SteelPyIntegrationFixed import STEELPY_AVAILABLE
        if STEELPY_AVAILABLE:
            print("✅ steelpy available and working")
        else:
            print("⚠️ steelpy not available - install with: pip install steelpy")
    except Exception as e:
        print(f"❌ steelpy integration error: {e}")
    
    # Check FreeCADGui
    try:
        import FreeCADGui as Gui
        print("✅ FreeCADGui available")
    except:
        print("❌ FreeCADGui not available")
    
    # Check commands
    try:
        import FreeCADGui as Gui
        commands = Gui.listCommands()
        adv_commands = [cmd for cmd in commands if 'AdvancedSectionManager' in cmd]
        if adv_commands:
            print(f"✅ Commands found: {adv_commands}")
        else:
            print("⚠️ No Advanced Section Manager commands found")
    except:
        pass

# Main execution
if __name__ == "__main__":
    try:
        import FreeCAD
        print(f"🔧 Running in FreeCAD {FreeCAD.Version()}")
        
        show_debug_info()
        success = run_quick_section_manager()
        
        if not success:
            print("\n💡 หากยังไม่ได้ ลองรันในบรรทัดถัดไป:")
            print("exec(open(r'C:\\Users\\thani\\AppData\\Roaming\\FreeCAD\\Mod\\StructureTools\\debug_gui.py').read())")
            
    except ImportError:
        print("⚠️ This should be run from FreeCAD Python console")
        print("Copy and paste this code into FreeCAD:")
        print("exec(open(r'C:\\Users\\thani\\AppData\\Roaming\\FreeCAD\\Mod\\StructureTools\\quick_section_manager.py').read())")

# Quick functions for direct use
def taskpanel():
    """Quick function: เปิด TaskPanel"""
    return method1_taskpanel()

def gui():
    """Quick function: เปิด GUI"""  
    return method3_direct_gui()

def cmd():
    """Quick function: เปิดด้วย Command"""
    return method2_command()

print("\n🚀 Quick Functions:")
print("taskpanel() - เปิด TaskPanel")
print("gui() - เปิด GUI")  
print("cmd() - เปิดด้วย Command")
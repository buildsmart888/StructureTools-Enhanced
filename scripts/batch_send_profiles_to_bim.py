"""Batch create ArchProfiles for imported sections and send to BIMIntegration bridge.

Run inside FreeCAD's Python console or with FreeCAD's python executable.

This script is conservative: it checks for Enhanced DB and BIMIntegration availability.
"""
import sys
import traceback

try:
    from freecad.StructureTools.data.EnhancedSteelDatabase import get_enhanced_database, get_enhanced_shape_types, get_enhanced_sections, get_enhanced_section_data, get_section_geometry_data
    from freecad.StructureTools.geometry.SectionDrawing import SectionDrawer
    from freecad.StructureTools.integration.BIMIntegration import BIMStructuralIntegration
except Exception as e:
    print("Required modules not available. Run inside FreeCAD with StructureTools loaded.")
    print(e)
    raise

def batch_send_all_imported():
    db = get_enhanced_database()
    shape_types = get_enhanced_shape_types()
    drawer = SectionDrawer()
    bridge = BIMStructuralIntegration()

    # Look for shape_type 'IMPORTED'
    if 'IMPORTED' not in shape_types:
        print('No IMPORTED shape type found in enhanced DB')
        return

    sections = get_enhanced_sections('IMPORTED')
    print(f'Found {len(sections)} IMPORTED sections; sending up to 100 (to avoid long runs)')

    sent = 0
    for name in sections[:100]:
        try:
            geom = get_section_geometry_data('IMPORTED', name)
            profile = None
            if geom and 'drawing_points' in geom:
                profile = drawer.create_arch_profile_from_points(geom['drawing_points'], name)

            if not profile and geom and geom.get('beam_type') == 'CIRCULAR' and 'outer_diameter' in geom:
                # approximate circle
                import math
                od = geom.get('outer_diameter')
                pts = [(od/2.0*math.cos(2*math.pi*i/32.0), od/2.0*math.sin(2*math.pi*i/32.0)) for i in range(32)]
                profile = drawer.create_arch_profile_from_points(pts, name)

            if profile:
                # attach standardized props if available
                props = get_enhanced_section_data('IMPORTED', name)
                try:
                    if hasattr(profile, 'addProperty'):
                        profile.addProperty('App::PropertyPythonObject', 'EnhancedProperties', 'BIM', 'Enhanced section properties')
                        profile.EnhancedProperties = props
                except Exception:
                    pass

                bridge.import_from_bim([profile])
                sent += 1
                print(f'Sent profile {name} to BIMIntegration')

        except Exception as e:
            print(f'Failed to send {name}: {e}')
            traceback.print_exc()

    print(f'Done. Sent {sent} profiles.')

if __name__ == '__main__':
    batch_send_all_imported()

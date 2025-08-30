
# ตรวจสอบ support nodes ในโมเดล FreeCAD
import FreeCAD as App

# สำหรับการ debug reaction nodes
def check_support_nodes():
    doc = App.ActiveDocument
    if not doc:
        print("No active document")
        return
    
    print("=== Checking Support Nodes ===")
    
    # หา calc object
    calc_obj = None
    for obj in doc.Objects:
        if hasattr(obj, "Proxy") and str(type(obj.Proxy)).find("Calc") != -1:
            calc_obj = obj
            break
    
    if not calc_obj:
        print("No Calc object found")
        return
        
    print(f"Found Calc object: {calc_obj.Label}")
    
    # ตรวจสอบ reaction data
    if hasattr(calc_obj, "ReactionNodes"):
        print(f"Reaction Nodes: {calc_obj.ReactionNodes}")
        print(f"Number of reaction nodes: {len(calc_obj.ReactionNodes)}")
        
        if hasattr(calc_obj, "ReactionX"):
            print("
Reaction Forces:")
            for i, node in enumerate(calc_obj.ReactionNodes):
                fx = calc_obj.ReactionX[i] if i < len(calc_obj.ReactionX) else 0
                fy = calc_obj.ReactionY[i] if i < len(calc_obj.ReactionY) else 0  
                fz = calc_obj.ReactionZ[i] if i < len(calc_obj.ReactionZ) else 0
                print(f"{node}: Fx={fx:.2f}, Fy={fy:.2f}, Fz={fz:.2f}")
                
        if hasattr(calc_obj, "ReactionMX"):
            print("
Reaction Moments:")  
            for i, node in enumerate(calc_obj.ReactionNodes):
                mx = calc_obj.ReactionMX[i] if i < len(calc_obj.ReactionMX) else 0
                my = calc_obj.ReactionMY[i] if i < len(calc_obj.ReactionMY) else 0
                mz = calc_obj.ReactionMZ[i] if i < len(calc_obj.ReactionMZ) else 0
                print(f"{node}: Mx={mx:.2f}, My={my:.2f}, Mz={mz:.2f}")
    
    # ตรวจสอบ support objects
    print("
=== Support Objects ===")
    support_count = 0
    for obj in doc.Objects:
        if "Suport" in obj.Name or "Support" in obj.Name:
            print(f"Found support: {obj.Label} ({obj.Name})")
            if hasattr(obj, "Position"):
                print(f"  Position: {obj.Position}")
            if hasattr(obj, "SupportType"):
                print(f"  Type: {obj.SupportType}")
            support_count += 1
            
    print(f"Total supports found: {support_count}")

if __name__ == "__main__":
    check_support_nodes()

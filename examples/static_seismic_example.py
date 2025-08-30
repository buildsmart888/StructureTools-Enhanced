"""
Example script demonstrating the new static seismic analysis functionality
"""

import sys
import os

# Add the module path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'freecad', 'StructureTools'))

def demonstrate_static_seismic_analysis():
    """Demonstrate the static seismic analysis functionality"""
    
    print("Static Seismic Analysis Example")
    print("=" * 40)
    
    try:
        # Import the static seismic modules
        from seismic.static_seismic import StaticSeismicParameters, StaticSeismicAnalyzer
        
        # Create building parameters
        print("1. Creating building parameters...")
        params = StaticSeismicParameters(
            building_height=30.0,      # 30 meters tall
            total_weight=50000.0,      # 50,000 kN total weight
            number_of_stories=10,      # 10-story building
            sds=1.0,                   # SDS = 1.0g
            sd1=0.4,                   # SD1 = 0.4g
            site_class="C",            # Site class C
            r_factor=8.0,              # Response modification factor
            importance_factor=1.0,     # Importance factor
            distribution_method="ASCE 7-22"  # Distribution method
        )
        
        print(f"   Building height: {params.building_height} m")
        print(f"   Total weight: {params.total_weight} kN")
        print(f"   Number of stories: {params.number_of_stories}")
        print(f"   SDS: {params.sds}g, SD1: {params.sd1}g")
        print(f"   Site class: {params.site_class}")
        print(f"   R factor: {params.r_factor}")
        print(f"   Importance factor: {params.importance_factor}")
        
        # Create analyzer
        print("\n2. Creating seismic analyzer...")
        analyzer = StaticSeismicAnalyzer(params)
        
        # Calculate fundamental period
        print("\n3. Calculating fundamental period...")
        period = analyzer.calculate_fundamental_period()
        print(f"   Fundamental period: {period:.3f} seconds")
        
        # Calculate seismic coefficient
        print("\n4. Calculating seismic coefficient...")
        cs = analyzer.calculate_seismic_coefficient()
        print(f"   Seismic coefficient (Cs): {cs:.4f}")
        
        # Calculate base shear
        print("\n5. Calculating base shear...")
        base_shear = analyzer.calculate_base_shear()
        print(f"   Base shear: {base_shear:.1f} kN")
        
        # Calculate story forces
        print("\n6. Calculating story forces...")
        story_forces = analyzer.calculate_story_forces()
        print(f"   Story forces calculated for {len(story_forces)} stories")
        
        # Calculate vertical force
        print("\n7. Calculating vertical seismic component...")
        vertical_force = analyzer.calculate_vertical_force()
        print(f"   Vertical seismic force: {vertical_force:.1f} kN")
        
        # Perform complete analysis
        print("\n8. Performing complete analysis...")
        results = analyzer.perform_analysis()
        
        print(f"\n   Analysis Results:")
        print(f"   - Fundamental Period: {results['period']:.3f} sec")
        print(f"   - Base Shear: {results['base_shear']:.1f} kN")
        print(f"   - Vertical Force: {results['vertical_force']:.1f} kN")
        
        # Get story data table
        print("\n9. Generating story data table...")
        story_data = analyzer.get_story_data_table()
        
        print(f"\n   Story Forces Distribution:")
        print(f"   {'Story':<6} {'Height (m)':<10} {'Weight (kN)':<12} {'Force (kN)':<12} {'Percentage (%)':<15}")
        print(f"   {'-'*6} {'-'*10} {'-'*12} {'-'*12} {'-'*15}")
        for row in story_data:
            print(f"   {row['story']:<6} {row['height']:<10.1f} {row['weight']:<12.1f} {row['force']:<12.1f} {row['percentage']:<15.1f}")
        
        print("\n✅ Static seismic analysis completed successfully!")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("   Make sure the StructureTools module is properly installed.")
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        import traceback
        traceback.print_exc()

def demonstrate_different_distribution_methods():
    """Demonstrate different story force distribution methods"""
    
    print("\n\nDistribution Methods Comparison")
    print("=" * 40)
    
    try:
        from seismic.static_seismic import StaticSeismicParameters, StaticSeismicAnalyzer
        
        # Common parameters
        base_params = {
            'building_height': 30.0,
            'total_weight': 50000.0,
            'number_of_stories': 5,
            'sds': 1.0,
            'sd1': 0.4,
            'r_factor': 8.0,
            'importance_factor': 1.0
        }
        
        methods = ["ASCE 7-22", "Linear", "Uniform"]
        
        for method in methods:
            print(f"\n{method} Distribution Method:")
            print("-" * 30)
            
            params = StaticSeismicParameters(
                distribution_method=method,
                **base_params
            )
            
            analyzer = StaticSeismicAnalyzer(params)
            story_forces = analyzer.calculate_story_forces()
            
            # Calculate percentages
            total_force = sum(story_forces)
            percentages = [100 * f / total_force for f in story_forces] if total_force > 0 else [0] * len(story_forces)
            
            for i, (force, percent) in enumerate(zip(story_forces, percentages)):
                story_num = len(story_forces) - i
                print(f"   Story {story_num}: {force:>8.1f} kN ({percent:>5.1f}%)")
                
    except Exception as e:
        print(f"❌ Error in distribution methods demonstration: {e}")

if __name__ == "__main__":
    demonstrate_static_seismic_analysis()
    demonstrate_different_distribution_methods()
    
    print("\n" + "=" * 50)
    print("Example completed!")
    print("This demonstrates the core functionality of the static seismic analysis module.")
    print("In the full GUI implementation, these calculations are integrated with")
    print("professional visualization and interactive controls.")
    print("=" * 50)
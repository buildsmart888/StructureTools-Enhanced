
class LoadCombinationManager:
    """
    Manages structural load combinations for analysis.
    Supports Allowable Stress Design (ASD) and Strength Design (LRFD).
    """

    def __init__(self):
        # Load combinations configuration
        self.load_combinations = {
            # Allowable Stress Design (100 series)
            '100_DL': {'DL': 1.0, 'LL': 0.0, 'W': 0.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '101_DL+LL': {'DL': 1.0, 'LL': 1.0, 'W': 0.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '102_DL+0.75(LL+W(X+))': {'DL': 1.0, 'LL': 0.75, 'W': 0.75, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '103_DL+0.75(LL+W(x-))': {'DL': 1.0, 'LL': 0.75, 'W': 0.75, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '104_DL+0.75(LL+W(y+))': {'DL': 1.0, 'LL': 0.75, 'W': 0.75, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '105_DL+0.75(LL+W(y-))': {'DL': 1.0, 'LL': 0.75, 'W': 0.75, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '106_0.6DL+W(X+)': {'DL': 0.6, 'LL': 0.0, 'W': 1.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '107_0.6DL+W(x-)': {'DL': 0.6, 'LL': 0.0, 'W': 1.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '108_0.6DL+W(y+)': {'DL': 0.6, 'LL': 0.0, 'W': 1.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '109_0.6DL+W(y-)': {'DL': 0.6, 'LL': 0.0, 'W': 1.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '110_DL+0.7E(X+)': {'DL': 1.0, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
            '111_DL+0.7E(x-)': {'DL': 1.0, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
            '112_DL+0.7E(y+)': {'DL': 1.0, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
            '113_DL+0.7E(y-)': {'DL': 1.0, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
            '114_DL+0.525E(X+)+0.75LL': {'DL': 1.0, 'LL': 0.75, 'W': 0.0, 'E': 0.525, 'H': 0.0, 'F': 0.0},
            '115_DL+0.525E(x-)+0.75LL': {'DL': 1.0, 'LL': 0.75, 'W': 0.0, 'E': 0.525, 'H': 0.0, 'F': 0.0},
            '116_DL+0.525E(Z+)+0.75LL': {'DL': 1.0, 'LL': 0.75, 'W': 0.0, 'E': 0.525, 'H': 0.0, 'F': 0.0},
            '117_DL+0.525E(z-)+0.75LL': {'DL': 1.0, 'LL': 0.75, 'W': 0.0, 'E': 0.525, 'H': 0.0, 'F': 0.0},
            '118_0.6DL+0.7E(X+)': {'DL': 0.6, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
            '119_0.6DL+0.7E(x-)': {'DL': 0.6, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
            '120_0.6DL+0.7E(y+)': {'DL': 0.6, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
            '121_0.6DL+0.7E(y-)': {'DL': 0.6, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
            '122_DL+LL+H+F': {'DL': 1.0, 'LL': 1.0, 'W': 0.0, 'E': 0.0, 'H': 1.0, 'F': 1.0},
            
            # Strength Design (1000 series)
            '1000_1.4DL': {'DL': 1.4, 'LL': 0.0, 'W': 0.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '1001_1.4DL+1.7LL': {'DL': 1.4, 'LL': 1.7, 'W': 0.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '1002_1.05DL+1.275LL+1.6W(x+)': {'DL': 1.05, 'LL': 1.275, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '1003_1.05DL+1.275LL+1.6W(x-)': {'DL': 1.05, 'LL': 1.275, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '1004_1.05DL+1.275LL+1.6W(y+)': {'DL': 1.05, 'LL': 1.275, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '1005_1.05DL+1.275LL+1.6W(y-)': {'DL': 1.05, 'LL': 1.275, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '1006_0.9DL+1.6W(X+)': {'DL': 0.9, 'LL': 0.0, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '1007_0.9DL+1.6W(x-)': {'DL': 0.9, 'LL': 0.0, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '1008_0.9DL+1.6W(y+)': {'DL': 0.9, 'LL': 0.0, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '1009_0.9DL+1.6W(y-)': {'DL': 0.9, 'LL': 0.0, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
            '1010_1.05DL+1.275LL+E(x+)': {'DL': 1.05, 'LL': 1.275, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
            '1011_1.05DL+1.275LL+E(x-)': {'DL': 1.05, 'LL': 1.275, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
            '1012_1.05DL+1.275LL+E(y+)': {'DL': 1.05, 'LL': 1.275, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
            '1013_1.05DL+1.275LL+E(y-)': {'DL': 1.05, 'LL': 1.275, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
            '1014_0.9DL+E(X+)': {'DL': 0.9, 'LL': 0.0, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
            '1015_0.9DL+E(x-)': {'DL': 0.9, 'LL': 0.0, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
            '1016_0.9DL+E(y+)': {'DL': 0.9, 'LL': 0.0, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
            '1017_0.9DL+E(y-)': {'DL': 0.9, 'LL': 0.0, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
            '1018_1.4DL+1.7LL+1.7H': {'DL': 1.4, 'LL': 1.7, 'W': 0.0, 'E': 0.0, 'H': 1.7, 'F': 0.0},
            '1019_0.9DL+1.7H': {'DL': 0.9, 'LL': 0.0, 'W': 0.0, 'E': 0.0, 'H': 1.7, 'F': 0.0},
            '1020_1.4DL+1.7LL+1.4F': {'DL': 1.4, 'LL': 1.7, 'W': 0.0, 'E': 0.0, 'H': 0.0, 'F': 1.4},
            '1021_0.9DL+1.4F': {'DL': 0.9, 'LL': 0.0, 'W': 0.0, 'E': 0.0, 'H': 0.0, 'F': 1.4}
        }

    def get_load_factor(self, load_case_or_combination, load_type):
        """
        Returns load factor for given load case/combination and load type.
        
        Args:
            load_case_or_combination (str): The name/ID of the load combo
            load_type (str): The type of load (DL, LL, W, etc.)
            
        Returns:
            float: The applicable load factor, defaults to 1.0 if not found explicitly but combo exists,
                   or 0.0 if load type not in combo? Original code returned 0.0 if found, else 1.0 if combo check failed (logic was slightly ambiguous).
                   Refactored to be precise: return defined factor or 0.0.
        """
        if load_case_or_combination in self.load_combinations:
            return self.load_combinations[load_case_or_combination].get(load_type, 0.0)
        
        # Default fallback (preserve legacy behavior if needed, or stricter?)
        # Original code: if key in dict returns dict[key].get(type, 0.0). else return 1.0
        return 1.0

    def get_analysis_type(self, load_combination):
        """Determine if ASD or Strength Design."""
        if not load_combination:
            return "Unknown"
        if load_combination.startswith('1') and not load_combination.startswith('10'):
            return "Allowable Stress Design"
        elif load_combination.startswith('10'):
            return "Strength Design"
        return "Allowable Stress Design"

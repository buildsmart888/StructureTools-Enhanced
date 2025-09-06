# Load Position Fix for StructureTools

## Issue Summary
When setting StartPosition to a value greater than EndPosition (like StartPosition=2000mm and EndPosition=0mm) in a distributed load, the arrows were being rendered outside the line.

## Root Cause
The original code had the following issues:
1. It forced EndPosition to always be greater than or equal to StartPosition with the line:
   ```python
   end_pos = max(start_pos, min(end_pos, subelement.Length))
   ```
   This meant that when a user set StartPosition > EndPosition, it would automatically use StartPosition for both.

2. The code only calculated distEndStart when end_pos > start_pos:
   ```python
   if end_pos > start_pos:
       distEndStart = end_pos - start_pos
   ```
   This meant that when start_pos was greater than end_pos, distEndStart would remain at its initial value of subelement.Length.

3. The step vector was only properly adjusted when end_pos > start_pos:
   ```python
   if end_pos > start_pos and subelement.Length > 0:
       scale_factor = (end_pos - start_pos) / subelement.Length
       step_vec.multiply(scale_factor)
   ```

## Implemented Fix
1. Added code to swap StartPosition and EndPosition when StartPosition > EndPosition:
   ```python
   if start_pos > end_pos:
       # Swap start and end positions
       temp = start_pos
       start_pos = end_pos
       end_pos = temp
   ```

2. Added special handling for the case when start_pos equals end_pos:
   ```python
   # If start and end are the same, use full length
   if distEndStart == 0:
       start_pos = 0.0
       end_pos = subelement.Length
       distEndStart = subelement.Length
   ```

3. Updated the step vector calculation to be more robust:
   ```python
   if distEndStart > 0 and subelement.Length > 0:
       scale_factor = distEndStart / subelement.Length
       step_vec.multiply(scale_factor)
   ```

4. Added position information to the load label to provide better user feedback:
   ```python
   if actual_end > 0:
       obj.Label = f'{obj.LoadType} distributed load ({obj.GlobalDirection}) [{actual_start}-{actual_end}]'
   else:
       obj.Label = f'{obj.LoadType} distributed load ({obj.GlobalDirection}) [{actual_start}]'
   ```

5. Added a warning message when StartPosition > EndPosition to inform the user that positions will be swapped for visualization:
   ```python
   if obj.StartPosition.Value > obj.EndPosition.Value and obj.EndPosition.Value > 0:
       FreeCAD.Console.PrintWarning("StartPosition is greater than EndPosition. The visualization will swap them.\n")
   ```

## Similar Changes for Point Loads
- Added more robust handling of relative position for point loads

## Benefits of the Fix
1. Users can now set StartPosition and EndPosition in any order, and the visualization will work correctly
2. When StartPosition equals EndPosition or EndPosition is zero, the load will be visualized over the full line
3. The load label now shows the positions, making it clearer to the user what portion of the line is loaded
4. Warning messages help users understand what's happening when positions are swapped

## Testing Instructions
1. Create a line in FreeCAD
2. Add a distributed load to the line
3. Set StartPosition to 2000mm and EndPosition to 0mm
4. The load should be visualized correctly, with arrows appearing only on the first 2000mm of the line
5. Try various combinations of StartPosition and EndPosition to verify proper behavior
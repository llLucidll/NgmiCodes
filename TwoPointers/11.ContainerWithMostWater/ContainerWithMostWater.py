def maxArea(height: List[int]) -> int:
    area = 0
    l = 0
    r = len(height) - 1

    while l < r:
        # Calculate the width 
        width = r - l
        # Calculate the current area
        current = min(height[l],height[r]) * width
        # Update area if current > area.
        area = max(current, area)

        if height[l] > height[r]:
            r -= 1
        else:
            l -= 1
    
    return area
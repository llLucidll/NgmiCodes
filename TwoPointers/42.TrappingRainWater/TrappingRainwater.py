def trap(self, height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    l_max = height[l]
    r_max = height[r]
    water = 0

    while l < r:
        if l_max > r_max:
            r -= 1
            r_max = max(r_max, height[r])
            water += height[r] - r_max
        
        else:
            l += 1
            l_max = max(l_max, height[l])
            water += height[l] - l_max
            
    return water
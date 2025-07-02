def largestRectangleArea(heights) -> int:
    maxArea = 0
    stack = []
    n = len(heights)

    for i in range(n+1):
        while stack and (i == n or heights[stack[-1]] >= heights[i]):
            height = heights[stack.pop()]
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            maxArea = max(maxArea, height * width)

        stack.append(i)
    
    return maxArea
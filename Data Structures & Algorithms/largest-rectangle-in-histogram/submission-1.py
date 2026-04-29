class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            print("---i: ", i)
            
            height = heights[i]
            width = 1
            # left check
            for j in range(i - 1, -1, -1):
                print("j: ", j)
                if heights[j] < height:
                    break
                width += 1
            # right check
            for k in range(i + 1, len(heights)):
                print("k: ", k)
                if heights[k] < height:
                    break
                width += 1
            area = height * width
            if maxArea < area:
                maxArea = area
            print(width, height, area)
        return maxArea
        
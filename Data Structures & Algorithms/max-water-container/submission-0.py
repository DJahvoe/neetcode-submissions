class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        biggestArea = 0

        while right > left:
            width = right - left
            height = min(heights[right], heights[left])
            tempArea = width * height
            if biggestArea < tempArea:
                biggestArea = tempArea
            
            if height == heights[right]:
                right -= 1
            else:
                left += 1
        
        return biggestArea
        
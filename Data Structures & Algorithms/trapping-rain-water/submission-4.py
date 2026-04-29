class Solution:
    def trap(self, height: List[int]) -> int:
        fillInList = [i for i in height]
        left = 0
        right = 1

        # left to right
        while left < len(height) - 1:            
            while right < len(height) and fillInList[left] > fillInList[right]:
                right += 1

            if right == len(height) and fillInList[left] > fillInList[right - 1]:
                left += 1
                right = left + 1
                continue
            maxHeight = min(fillInList[left], fillInList[right])
            for i in range(left + 1, right):
                print("i: ", i)
                fillInList[i] = maxHeight
            left = right
            right = left + 1
        print("After Left: ", fillInList)

        # right to left
        right = len(height) - 1
        left = right - 1
        while right > 0:
            while left >= 0 and fillInList[right] > fillInList[left]:
                left -= 1
            print("Pair: ", right, left)
            if left == -1 and fillInList[right] > fillInList[left + 1]:
                right -= 1
                left = right - 1
                continue
            maxHeight = min(fillInList[left], fillInList[right])
            for i in range(right - 1, left, -1):
                print(i)
                fillInList[i] = maxHeight
            right = left
            left = right - 1
        print("After Right: ", fillInList)
        vol = 0
        for i in range(len(height)):
            vol += fillInList[i] - height[i]
        return vol

        
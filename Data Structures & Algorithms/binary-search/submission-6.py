class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Edge case
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return (-1, 0)[nums[0] == target]
        elif len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1

        # General case
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while not(abs(left - right) <= 1):
            if nums[mid] == target:
                break
            elif target > nums[mid]:
                left = mid
            else:
                right = mid
            mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[right] == target:
            return right
        else:
            return -1

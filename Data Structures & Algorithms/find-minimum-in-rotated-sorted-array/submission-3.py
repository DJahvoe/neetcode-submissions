class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2

        # edge case
        if r == 0:
            return nums[0]
        if r == 1:
            return min(nums[0],nums[1])
        if nums[l] < nums[mid] and nums[mid] < nums[r]:
            return nums[l]

        while l != r:
            mid = (l + r) // 2
            print(l, r, mid)
            # left sorted segment, then smallest on the right sorted segment
            if nums[l] < nums[mid]:
                l = mid
            # right sorted segment, then smallest on the left sorted segment
            elif nums[mid] < nums[r]:
                r = mid
            else:
                break
        return nums[l + 1]

        

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # edge case
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1

        l = 0
        r = len(nums) - 1
        alrdAsc = False
        mid = (l + r) // 2
        if nums[l] < nums[mid] and nums[mid] < nums[r]:
            l = 0
            r = len(nums) - 1
            alrdAsc = True
        if not alrdAsc:
            # find pivot index
            while l <= r:
                mid = (l + r) // 2
                print("pivot")
                print(l, r, mid)

                if nums[l] < nums[mid]:
                    l = mid
                elif nums[mid] < nums[r]:
                    r = mid
                else:
                    break
            
            pivotIndex = l
            print(pivotIndex)
            if target >= nums[0]:
                l = 0
                r = pivotIndex
            else:
                l = pivotIndex + 1
                r = len(nums) - 1

        # find target
        while l <= r:
            mid = (l + r) // 2
            print("target")
            print(l, r, mid)
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        if nums[mid] == target:
            return mid
        return -1


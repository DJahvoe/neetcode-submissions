class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        i = 0
        j = i + 1
        k = len(nums) - 1
        
        while i < len(nums) - 2:
            # Search for the right sum
            target = -nums[i]
            searchSum = nums[j] + nums[k]
            if searchSum == target:
                isExist = False

                temp = [nums[i], nums[j], nums[k]]
                if len(result) > 0:
                    for arr in result:
                        if arr == temp:
                            isExist = True
                            break

                if not(isExist):
                    result.append(temp)
                k -= 1
            elif searchSum > target:
                k -= 1
            elif searchSum < target:
                j += 1

            # IF j and k the same, slide target
            if j == k:
                i += 1
                j = i + 1
                k = len(nums) - 1
        return result
        
class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0

        # Remove duplicates
        unique_nums = list(set(nums))

        # Sort the list using selection sort (as in your JS code)
        for i in range(len(unique_nums)):
            for j in range(i, len(unique_nums)):
                if unique_nums[i] > unique_nums[j]:
                    unique_nums[i], unique_nums[j] = unique_nums[j], unique_nums[i]

        # Assess longest consecutive sequence
        longest = 1
        temp_length = 1

        for i in range(len(unique_nums) - 1):
            if unique_nums[i] + 1 == unique_nums[i + 1]:
                temp_length += 1
            else:
                temp_length = 1
            longest = max(longest, temp_length)

        return longest

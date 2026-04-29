class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            next_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    curr = perm.copy()
                    curr.insert(i, n)
                    next_perms.append(curr)
            perms = next_perms
        return perms
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        p1 = len(nums) - 1
        p2 = p1 - 1

        i = 1
        while p1 >= 0 and p2 >= 0:
            print(p2, p1)
            
            if nums[p2] >= i:
                p1 = p2
                p2 = p1 - 1
                i = 1
                continue
            
            p2 -= 1
            i += 1
        print(p2, p1)
        return p1 == 0
        


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            print(q)
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                print("SMALLER")
                print(q)
                q.pop()
            q.append(r)

            # removes left val from window
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res
            
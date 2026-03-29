from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()
        l = 0
        for r in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()
            dq.append(r)
            if r-l+1 == k:
                res.append(nums[dq[0]])
                if l == dq[0]:
                    dq.popleft()
                l+=1
        return res


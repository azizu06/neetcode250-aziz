class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0:1}
        res = cur = 0
        for n in nums:
            cur += n
            diff = cur - k

            res += counts.get(diff, 0)
            counts[cur] = counts.get(cur, 0) + 1
        return res
            
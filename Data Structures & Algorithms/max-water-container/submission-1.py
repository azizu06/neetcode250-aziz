class Solution:
    def maxArea(self, heights: List[int]) -> int:
            l, r = 0, len(heights)-1
            res = 0
            while l < r:
                w = r-l
                h = min(heights[l], heights[r])
                res = max(h*w, res)
                if heights[l] > heights[r]:
                    r-=1
                else:
                    l+=1
            return res
                
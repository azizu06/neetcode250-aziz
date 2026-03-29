class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0]*n
        right = [n-1]*n
        s = []
        for i in range(n):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            if s:
                left[i] = s[-1]+1
            s.append(i)
        s = []
        for i in range(n-1, -1, -1):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            if s:
                right[i] = s[-1]-1
            s.append(i)
        res = 0
        for i in range(n):
            res = max(heights[i] * (right[i] - left[i] + 1), res)
        return res
            


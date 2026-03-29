class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        lMax = rMax = res = 0
        for i in range(len(height)):
            if height[i] > lMax:
                lMax = height[i]
            left[i] = lMax
        for i in range(len(height)-1, -1, -1):
            if height[i] > rMax:
                rMax = height[i]
            right[i] = rMax
        for i in range(len(height)):
            res += min(left[i], right[i]) - height[i]
        return res


        
            


            
            
            
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False
        a,b,c = target
        for t in triplets:
            if t[0] > a or t[1] > b or t[2] > c: continue
            if t[0] == a: x = True
            if t[1] == b: y = True
            if t[2] == c: z = True
        return x and y and z



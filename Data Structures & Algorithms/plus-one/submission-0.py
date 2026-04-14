class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        n = ''.join(digits)
        res = []
        for c in str(int(n)+1):
            res.append(int(c))
        return res
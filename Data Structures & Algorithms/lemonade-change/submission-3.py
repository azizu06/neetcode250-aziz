class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5: return False
        five = ten = twenty = 0
        for b in bills:
            cost = b-5
            if cost > (five*5)+(ten*10): return False
            if b == 5:
                five+=1
            elif b == 10:
                if not five: return False
                five-=1
                ten+=1
            else:
                if ten and five:
                    ten-=1
                    five-=1
                elif five > 2:
                    five-=3
                else:
                    return False
        return True

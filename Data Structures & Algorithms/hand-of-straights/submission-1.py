class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize: return False
        hand.sort()
        count = Counter(hand)
        for n in hand:
            if not count[n]: continue
            for i in range(groupSize):
                if not count[n+i]:
                    return False
                count[n+i]-=1
        return True
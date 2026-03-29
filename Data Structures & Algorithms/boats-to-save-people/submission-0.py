class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j, res = 0, len(people)-1, 0
        while i <= j:
            if people[i] + people[j] <= limit:
                i, j, res = i+1, j-1, res+1
            else:
                res, j, = res+1, j-1
        return res
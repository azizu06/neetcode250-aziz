class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1: return 1
        candy = [1]*n
        candy = [0]+candy+[0]
        ratings = [ratings[0]]+ratings+[ratings[n-1]]
        print(ratings)
        for i in range(1,n+1):
            if ratings[i] > ratings[i-1] and ratings[i] > ratings[i+1]:
                candy[i] = 1+max(candy[i-1],candy[i+1])
            elif ratings[i] > ratings[i-1]:
                candy[i] = 1+candy[i-1]
            elif ratings[i] > ratings[i+1]:
                candy[i] = 1+candy[i+1]
        for i in range(n,0,-1):
            if ratings[i] > ratings[i-1] and ratings[i] > ratings[i+1]:
                candy[i] = 1+max(candy[i-1],candy[i+1])
            elif ratings[i] > ratings[i-1]:
                candy[i] = 1+candy[i-1]
            elif ratings[i] > ratings[i+1]:
                candy[i] = 1+candy[i+1]

        return sum(candy)
from typing import List


class Solution:
    def solve(self,i,cost,w,dp):
        if w == 0:
            return 0
        if i >= len(cost) or i+1 > w :
            return 1e9
        if dp[i][w] != -1 :
            return dp[i][w]
        if cost[i] !=-1 and i+1<=w:
            a=cost[i]+self.solve(i,cost,w-(i+1),dp)
        b=self.solve(i+1,cost,w,dp)
        dp[i][w]=min(a,b)
        return dp[i][w]
    def minimumCost(self, n , w , cost ) :
        dp=[[-1 for _ in range(w+1)]for _ in range(n+1 )]
        ans=self.solve(0,cost,w,dp)
        if ans>=1e9 :
            return -1
        return ans
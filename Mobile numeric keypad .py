class Solution:
    def getCount(self, n):
        self.moves={
            "0":["0","8"],
            "1":["1","2","4"],
            "2":["1","2","3","5"],
            "3":["2","3","6"],
            "4":["1","4","5","7"],
            "5":["2","4","5","6","8"],
            "6":["3","5","6","9"],
            "7":["4","7","8"],
            "8":["5","7","8","9","0"],
            "9":["6","8","9"]
        }
        self.memo={}
        def dp(lastKey,length):
            if length == n:
                return 1
            if self.memo.get((lastKey,length)):
                return self.memo[(lastKey,length)]
            count=0
            for i in self.moves[lastKey]:
                count+=dp(i,length+1)
            self.memo[(lastKey,length)] = count
            return count
        res=0
        for key in "0123456789":
            res+=dp(key,1)
        return res
#  dp = [1]*10
       
#         for i in range(1, n):
#             temp = [0]*10
#             temp[0] = dp[0] + dp[8]
#             temp[1] = dp[1] + dp[2] + dp[4]
#             temp[2] = dp[1] + dp[2] + dp[3] + dp[5]
#             temp[3] = dp[2] + dp[3] + dp[6]
#             temp[4] = dp[1] + dp[4] + dp[5] + dp[7]
#             temp[5] = dp[2] + dp[4] + dp[5] + dp[6] + dp[8]
#             temp[6] = dp[3] + dp[5] + dp[6] + dp[9]
#             temp[7] = dp[4] + dp[7] + dp[8]
#             temp[8] = dp[5] + dp[7] + dp[8] + dp[9] + dp[0]
#             temp[9] = dp[6] + dp[8] + dp[9]
#             dp = temp
       
#         return sum(dp)
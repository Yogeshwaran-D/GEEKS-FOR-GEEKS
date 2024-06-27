class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        n,m,MOD=len(s1),len(s2),1000000007
        pre=[0]*(m+1)
        pre[m]=1
        for i in range(n-1,-1,-1):
            curr=[0]*(m+1)
            curr[m]=1
            for j in range(m-1,-1,-1):
                ans=pre[j]%MOD
                if s1[i]==s2[j]:
                    ans+=pre[j+1]%MOD
                curr[j]=ans%MOD
            pre=[k for k in curr]
        return curr[0]%MOD
        # st=""
        # for ele in s1 :
        #     if ele in s2:
        #         st+=ele
        # s1=st
        # self.res=0
        # def subset(i,j,temp):
        #     if temp == s2:
        #         self.res+=1
        #         return
        #     if i>=len(s1) or j>=len(s2):
        #         return
        #     if s1[i] == s2[j]:
        #         subset(i+1,j+1,temp+s1[i])
        #     subset(i+1,j,temp)
        # subset(0,0,"")
        # return self.res
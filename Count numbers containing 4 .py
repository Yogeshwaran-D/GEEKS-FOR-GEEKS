class Solution:
    def countNumberswith4(self, n ) :
        # code here
        res=0
        for i in range(1,n+1):
            for ele in str(i):
                if ele == "4" :
                    res+=1
                    break
        return res
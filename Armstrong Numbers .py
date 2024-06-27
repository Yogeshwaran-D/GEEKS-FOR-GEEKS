class Solution:
    def armstrongNumber (self, n):
        # code here 
        num=str(n)
        res=0
        l=len(num)
        for i in num:
            res+=(int(i))**l
        if res == n:
            return "true"
        else:
            return "false"
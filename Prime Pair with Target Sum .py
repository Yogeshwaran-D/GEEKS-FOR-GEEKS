class Solution:
    def getPrimes(self, n ) :
        # code here
        arr=[1]*(n+1)
        arr[0],arr[1]=0,0
        for i in range(2,n+1):
            if arr[i] == 0:
                continue
            j=2
            while j*i <=n:
                arr[j*i]=0
                j+=1
        for i in range(n):
            j=n-i
            if arr[i]==1 and arr[j] ==1 :
                return(i,j)
        return[-1,-1]
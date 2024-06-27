class Solution:
    def dfs(self,arr,index,k):
        if k == 0 :
            self.ans.append(self.current.copy())
            return
        if index==len(arr) or k<0 :
            return
        for i in range(index,len(arr)):
            if i>index and arr[i]==arr[i-1]:
                continue
            self.current.append(arr[i])
            self.dfs(arr,i+1,k-arr[i])
            self.current.pop()
    def CombinationSum2(self, arr, n, k):
        self.ans=[]
        self.current=[]
        arr=sorted(arr)
        self.dfs(arr,0,k)
        return self.ans
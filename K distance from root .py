class Solution:
    def KDistance(self,root,k):
        self.index=0
        self.lis=[]
        def search(root):
            if root == None : 
                    return
            if self.index == k:
                self.lis.append(root.data)
                return 
            self.index+=1
            search(root.left)
            search(root.right)
            self.index-=1
        search(root)
        return self.lis
    
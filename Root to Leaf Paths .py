class Solution:
    def PrintPath(self,node):
        if node == None :
            return 
        self.currentPath.append(node.data)
        if node.right == None and node.left == None :
            self.ans.append(self.currentPath[:])
        else:
            self.PrintPath(node.left)
            self.PrintPath(node.right)
        self.currentPath.pop()
    def Paths(self, root ):
        self.ans=[]
        self.currentPath=[]
        self.PrintPath(root)
        return self.ans
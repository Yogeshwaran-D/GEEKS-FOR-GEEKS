class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Solution:
    def consTree(self,post,ps,pe,In,Is,Ie,new_dict):
        if ps>pe or Is>Ie:
            return None
        root=Node(post[pe])
        rootIndex=new_dict.get(post[pe])
        leftEndIndex=rootIndex-Is
        root.left=self.consTree(post,ps,ps+leftEndIndex-1,In,Is,rootIndex-1,new_dict)
        root.right=self.consTree(post,ps+leftEndIndex,pe-1,In,rootIndex+1,Ie,new_dict)
        return root
    def buildTree(self,In, post, n):
        new_dict={}
        for i in range(n):
            new_dict[In[i]]=i
        return self.consTree(post,0,n-1,In,0,n-1,new_dict)
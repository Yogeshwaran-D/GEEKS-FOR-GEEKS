class Solution:
    
    def verticalSum(self, root):
        new_dict={}
        def LevelOrder(node,index):
            if node == None :
                return 
            LevelOrder(node.left,index-1)
            new_dict[index]=node.data+new_dict.get(index,0)
            LevelOrder(node.right,index+1)
        LevelOrder(root,0)
        lis=[]
        sorted_keys=sorted(new_dict.keys())
        for keys in sorted_keys:
            lis.append(new_dict[keys])
        return lis
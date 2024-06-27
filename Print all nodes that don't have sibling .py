def CheckSibling(node,lis):
    if node == None :
        return
    if  node.left != None and node.right != None :
        CheckSibling(node.left,lis)
        CheckSibling(node.right,lis)
    elif node.left != None:
        lis.append(node.left.data)
        CheckSibling(node.left,lis)
    elif node.right != None :
        lis.append(node.right.data)
        CheckSibling(node.right,lis)
    
def noSibling(root):
    lis=[]
    CheckSibling(root,lis)
    if lis :
        return sorted(lis)
    else:
        return [-1]
from typing import List
from collections import defaultdict

class Solution:
    def findNumberOfGoodComponent(self, e, v , edges ):
        root=list(range(v))
        degree=[0]*v
        group=defaultdict(list)
        def util(x):
            if root[x] == x :
                return x
            root[x]=util(root[x])
            return root[x]
        for i,j in edges:
            degree[i-1]+=1
            degree[j-1]+=1
            root[util(i-1)]=util(j-1)
        for i in range(v):
            group[util(i)].append(i)
        return sum(all(degree[x]==len(c)-1 for x in c)for c in group.values()) 
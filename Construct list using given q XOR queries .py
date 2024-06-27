from typing import List

class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
        res=[]
        xor=0
        for i in range(q-1,-1,-1):
            if queries[i] [0] == 1 :
                xor^=queries[i][1]
            else:
                res.append(queries[i][1]^xor)
        res.append(xor)
        res.sort()
        return res
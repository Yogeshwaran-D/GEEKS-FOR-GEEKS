class Solution:
    def rectanglesInCircle(self,r):
        temp=4*(r*r)
        res=0
        for x in range(1,2*r):
            for y in range(1,2*r):
                if (x*x) + (y*y) <= temp:
                    res+=1
        return res
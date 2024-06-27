class Solution:
    def minSteps(self, d):
        steps=0
        sum=0
        while sum<d or (sum-d)%2 !=0:
            steps+=1
            sum+=steps
        return steps
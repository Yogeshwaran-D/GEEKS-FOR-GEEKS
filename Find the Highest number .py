class Solution:
    def findPeakElement(self, a):
        for i in range(1,len(a)):
            if a[i]<a[i-1]:
                return a[i-1]
        return a[-1]
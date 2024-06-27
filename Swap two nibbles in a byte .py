class Solution:
    def swapNibbles (self, n):
        n=bin(n)[2:]
        f,s=n[-4:],n[:-4]
        while len(s)<4:
            s='0'+s
        num=f+s
        return int(num,2)
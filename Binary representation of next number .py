class Solution:
    def binaryNextNumber(self, s):
        n=int(s,2)
        n+=1
        n=bin(n)[2:]
        while n[0] == "0":
            n.pop(0)
        return n
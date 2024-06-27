class Solution:
    def jugglerSequence(self, n):
        ans=[n]
        while n!=1 :
            if n%2 == 0:
                n=int(n**(1/2))
            else:
                n=int(n**(3/2))
            ans.append(n)
        return ans
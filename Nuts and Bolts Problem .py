class Solution:
    def matchPairs(self, n, nuts, bolts):
        order={'!':0,'#':1,'$':2,'%':3,'&':4,
            '*':5,'?':6,'@':7,'^':8}
        arr=['!','#','$','%','&','*','?','@','^']
        res=[0]*n
        for i in range(n):
            res[i]=order.get(nuts[i])
        res.sort()
        for i in range(n):
            nuts[i]=arr[res[i]]
            bolts[i]=arr[res[i]]
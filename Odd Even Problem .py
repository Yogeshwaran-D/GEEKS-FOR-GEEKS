from collections import Counter
class Solution:
    def oddEven(self, s : str) -> str:
        new_dict=Counter(s)
        res=0
        s=set(s)
        for ele in s:
            if (ord(ele)-96) % 2 == new_dict.get(ele)%2:
                res+=1
        if res%2==0:
            return "EVEN"
        else:
            return "ODD"
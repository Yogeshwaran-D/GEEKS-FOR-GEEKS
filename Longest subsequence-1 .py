from typing import List


class Solution:
      def longestSubseq(self, n , a ) :
        prv=dict()
        mx=0
        for i in a:
            prv[i]=max(prv.get(i,1),prv.get(i-1,-1)+1,prv.get(i+1,-1)+1)
            mx=max(mx,prv[i])
        return mx
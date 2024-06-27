class Solution:
    def zigZag(self, n , arr ) :
        i=0
        while i<n:
            if i-1>-1:
                if arr[i]>arr[i-1]:
                    arr[i-1],arr[i]=arr[i],arr[i-1]
            if i+1<n:
                if arr[i]>arr[i+1]:
                    arr[i+1],arr[i]=arr[i],arr[i+1]
            i+=2
        # i=1
        # while i<n:
        #     if i-1>-1:
        #         if arr[i-1]>arr[i]:
        #             arr[i-1],arr[i]=arr[i],arr[i-1]
        #     if i+1<n:
        #         if arr[i+1]>arr[i]:
        #             arr[i+1],arr[i]=arr[i],arr[i+1]
        #     i+=2
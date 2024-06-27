class Solution:
    def findClosest(self, n , k , arr ) :
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]<k:
                low=mid+1
            else:
                high=mid-1
        if low<=n-1 and abs(k-arr[low]) <= abs(k-arr[high]):
            return arr[low]
        else:
            return arr[high]
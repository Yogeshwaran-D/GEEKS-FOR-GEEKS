class Solution:
    
    def check(self, mid, arr, k):
        n = len(arr)
        count = 0
        for i in range(1, n):
            dist = arr[i] - arr[i - 1]
            if dist <= mid:
                continue
            else:
                count += int(dist / mid)
        return count <= k
    def findSmallestMaxDist(self, stations, k):
        # Code here
        n = len(stations)
        lo = 0.0
        hi = 0.0
        for i in range(1, n):
            if hi < stations[i] - stations[i - 1]:
                hi = stations[i] - stations[i - 1]
        ans = hi
        while hi - lo > 1e-9:
            mid = (hi - lo) / 2.0 + lo
            if self.check(mid, stations, k):
                ans = mid
                hi = mid
            else:
                lo = mid
        return ans
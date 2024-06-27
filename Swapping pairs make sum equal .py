class Solution:
    def findSwapValues(self,a, n, b, m):
        suma = 0
        sumb = 0
        for i in range(n):
            suma += a[i]
        for i in range(m):
            sumb += b[i]

        if (suma - sumb) % 2 != 0:
            return -1
        target = (suma - sumb) // 2
        i = 0
        j = 0
        a.sort()
        b.sort()
        while i < n and j < m:
            diff = a[i] - b[j]
            if diff == target:
                return 1
            elif diff < target:
                i += 1
            else:
                j += 1
        return -1
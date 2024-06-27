from typing import List
import heapq

class Solution:
    def MinimumEffort(self,rows, columns, heights):
        def canReachEnd(mid):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            visited = [[False] * columns for _ in range(rows)]
            min_heap = [(0, 0, 0)]  # (effort, row, col)
            while min_heap:
                effort, x, y = heapq.heappop(min_heap)
                if x == rows - 1 and y == columns - 1:
                    return True
                if visited[x][y]:
                    continue
                visited[x][y] = True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < columns and not visited[nx][ny]:
                        current_effort = abs(heights[nx][ny] - heights[x][y])
                        if current_effort <= mid:
                            heapq.heappush(min_heap, (max(effort, current_effort), nx, ny))
            return False
        
        low, high = 0, max(max(row) for row in heights)
        while low < high:
            mid = (low + high) // 2
            if canReachEnd(mid):
                high = mid
            else:
                low = mid + 1
        return low
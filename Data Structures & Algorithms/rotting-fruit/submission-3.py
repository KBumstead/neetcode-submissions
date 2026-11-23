class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        fresh = set()
        minute = 0
        q = deque()

        def addGrid(r,c):
            if(
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0 or
                (r,c) in visited
            ):
                return
            fresh.remove((r,c))
            visited.add((r,c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:    
                    fresh.add((r,c))
                if grid[r][c] == 2 and (r,c) not in visited:
                    visited.add((r,c))
                    q.append([r,c])
                
        
        while q and fresh:
            for i in range(len(q)):
                r,c = q.popleft()
                addGrid(r + 1, c)
                addGrid(r - 1, c)
                addGrid(r, c + 1)
                addGrid(r, c - 1)

            minute += 1

        if fresh:
            return -1
        return minute


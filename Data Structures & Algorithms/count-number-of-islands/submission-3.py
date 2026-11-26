class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        island = 0

        def dfs(r,c):
            if(
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == "0" or
                (r, c) in visited
            ):
                return

            visited.add((r,c))
            directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0,-1]
            ]
                
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    island += 1

        return island

         
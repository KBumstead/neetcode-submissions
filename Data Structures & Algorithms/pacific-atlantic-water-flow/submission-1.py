class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pac = set()
        atl = set()

        def dfs(row, col, visited, prevHeight):
            if (
                row < 0 or col < 0 or
                row >= ROWS or col >= COLS or 
                (row, col) in visited or
                heights[row][col] < prevHeight
            ):
                return

            visited.add((row,col))

            directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]

            for dr, dc in directions:
                dfs(row + dr, col + dc, visited, heights[row][col])

        for row in range(ROWS):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, COLS - 1, atl, heights[row][COLS - 1])

        for col in range(COLS):
            dfs(0, col, pac, heights[0][col])
            dfs(ROWS - 1, col, atl, heights[ROWS -1][col])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res

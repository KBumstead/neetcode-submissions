class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r,c, visited, flag):
            if (r,c) in visited:
                return
            
            visited.add((r,c))
            
            #flag 0 for atlantic
            #flag 1 for pacific
            if(r == ROWS - 1):
                flag[0] = 1
                
            if (r - 1 < 0):
                flag[1] = 1
                
            if (c == COLS - 1):
                flag[0] = 1
                
            if (c - 1 < 0):
                flag[1] = 1
                

            directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]

            for dr, dc in directions:
                row, col = r + dr, c + dc

                if(row >= ROWS or col >= COLS or row < 0 or col < 0):
                    continue

                if (heights[r][c] < heights[row][col]):
                    continue

                dfs(row, col, visited, flag)
            
            
        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                flag = [0,0]
                dfs(r, c, visited, flag)
                if flag[0] == 1 and flag[1] == 1:
                    res.append([r,c])



        return res
        


        
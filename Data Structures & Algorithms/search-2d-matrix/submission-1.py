class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) -1
        
        while( l <= r):
            mid = (l + r )// 2
            numCols = len(matrix[0])
            row = mid // numCols
            col = mid % numCols

            if(target == matrix[row][col]):
                return True
            elif target < matrix[row][col]:
                r = mid - 1
            elif target > matrix[row][col]:
                l = mid + 1

        return False





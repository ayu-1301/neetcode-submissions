class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row*col - 1

        while left <= right:
            mid = left + (right - left)//2
            val = matrix[mid//col][mid%col]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = right - 1
            
        return False
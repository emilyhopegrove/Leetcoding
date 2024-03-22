class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1

        # First, find the correct row using binary search.
        while top <= bottom:
            midRow = (top + bottom) // 2
            if target > matrix[midRow][-1]:  # If target is greater than the last element of the mid row
                top = midRow + 1
            elif target < matrix[midRow][0]:  # If target is less than the first element of the mid row
                bottom = midRow - 1
            else:
                break  # Target must be in this row

        if not (top <= bottom):
            return False  # Target is not in any row

        # Now, top == bottom and it indicates the target row.
        row = (top + bottom) // 2
        left, right = 0, cols - 1

        # Conduct binary search in the identified row.
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True  # Target found

        return False  # Target not found in the row

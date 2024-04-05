from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:  # 判断矩阵是否为空
            return False

        rows, cols = len(matrix), len(matrix[0])

        # 从顶部行开始，使用二分查找法定位可能包含目标值的行
        low, high = 0, rows - 1
        while low <= high:
            mid_row = low + (high - low) // 2
            mid_val = matrix[mid_row][0]

            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid_row + 1
            else:
                high = mid_row - 1

        # 获取最有可能包含目标值的行（low - 1是因为low已经指向了可能的下一行）
        row = low - 1 if target > matrix[low][0] else high

        # 在找到的行内进行二分查找
        left, right = 0, cols - 1
        while left <= right:
            mid_col = left + (right - left) // 2
            cell_value = matrix[row][mid_col]

            if cell_value == target:
                return True
            elif cell_value < target:
                left = mid_col + 1
            else:
                right = mid_col - 1

        # 如果没有找到目标值，则返回False
        return False
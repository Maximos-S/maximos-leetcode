class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            return self.searchRow(matrix[0], target)

        mid = math.floor(len(matrix) / 2)

        if target == matrix[mid][0]:
            return True
        elif target < matrix[mid][0]:
            return self.searchMatrix(matrix[0:mid], target)
        else:
            return self.searchMatrix(matrix[mid:], target)

    def searchRow(self, row, target):
        if not len(row):
            return False
        if len(row) <= 1:
            if row[0] == target:
                return True
            return False
        mid = math.floor(len(row) / 2)
        print(mid)
        print(row)
        if target == row[mid]:
            return True
        elif target < row[mid]:
            return self.searchRow(row[0:mid], target)
        else:
            return self.searchRow(row[mid+1:], target)

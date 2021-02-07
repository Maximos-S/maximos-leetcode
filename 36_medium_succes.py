class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 1
        while i < 9:
            j = 1
            while j < 9:
                if not self.squareIsValid(board, i, j):
                    print("square isn't valid")
                    return False
                j += 3
            i += 3

        for column_or_row in range(9):
            if not self.columnIsValid(board, column_or_row):
                print("Column isn't valid")
                return False
            if not self.rowIsValid(board, column_or_row):
                print("Row isn't valid")
                return False

        return True

    def squareIsValid(self, board, column, row):
        contents = []

        contents.append(board[column][row])
        contents.append(board[column][row - 1])
        contents.append(board[column][row + 1])
        contents.append(board[column + 1][row - 1])
        contents.append(board[column + 1][row])
        contents.append(board[column + 1][row + 1])
        contents.append(board[column - 1][row - 1])
        contents.append(board[column - 1][row])
        contents.append(board[column - 1][row + 1])
        nums = []
        for content in contents:
            if content == ".":
                continue
            else:
                nums.append(content)

        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                if nums[i] == nums[j]:
                    return False
                j += 1
        return True

    def columnIsValid(self, board, column):
        nums = []
        for row in range(9):
            if board[column][row] == ".":
                continue
            else:
                nums.append(board[column][row])

        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                if nums[i] == nums[j]:
                    return False
                j += 1
        return True

    def rowIsValid(self, board, row):
        nums = []
        for column in range(9):
            if board[column][row] == ".":
                continue
            else:
                nums.append(board[column][row])

        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                if nums[i] == nums[j]:
                    return False
                j += 1
        return True

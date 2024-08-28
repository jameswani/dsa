from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len, col_len = len(board), len(board[0])
        index = 0

        visited = set()

        def dfs(index, row, column)
            if row < 0 or row >= len(board) or column < 0 or column >= len(board): # type: ignore
                return False
            if board[row][column] != word[index] or (row,column) in visited:
                return False
            if index == len(word) -1:
                return True
            
            visited.add(row,column)

            for dr, dc in neighbors:
                nrow, ncol = r + dr, c + dc
                

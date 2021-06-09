'''
Task Details
    Platform: LeetCode
    Name: 1252. Cells with Odd Values in a Matrix 
    Link: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
'''

class Solution:
    def increment_row(self, matrix, row):
        for i in range(len(matrix[0])):
            matrix[row][i] += 1
    
    def increment_col(self, matrix, col):
        for i in range(len(matrix)):
            matrix[i][col] += 1
    
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        matrix = [[0 for i in range(m)] for j in range(n)]
        #print(f'Org : {matrix}')
        for i in indices:
            #print(f'After : {i}')            
            self.increment_row(matrix, i[0])            
            #print(f'After Row Inc : {matrix}')            
            self.increment_col(matrix, i[1])
            #print(f'After Col Inc : {matrix}')

        odd_count = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2 != 0:
                    odd_count += 1
        return odd_count

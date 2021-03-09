# Author: Diego Saldonid
# Date: 3/3/2021
# Description: Algorithm solves any sudoku

def solve(self,board,row,col):
	'''
	Function that uses backtracking in order to solve any sudoku puzzle. 
	Inputs: the current board,the current row and column

	'''

		#if our column is 
        if col > 8 or (col ==8 and board[row][col]!= '.'):
            return self.solve(board,row+1,0)
        elif row >8:
            return True
        elif board[row][col] != '.':
            return self.solve(board,row,col+1)
    
        for i in range(1,10):
            uni = unicode(i)
            board[row][col] = uni
            if self.isValidSudoku(board):
                if self.solve(board,row,col+1):
                    return True 
            board[row][col] = '.'
        return False
            

def isValidSudoku(self, board):
    """
    inputs: the current board
    returns: True is the current board is valid or False if it is not 
    """

    #create our nine boxes that we will add to to with every value seen
    boxes = [[set(),set(),set()],
            [set(),set(),set()],
            [set(),set(),set()]]

    #loop through all rows to make sure our contraints aren't violated
    for row in range(len(board)):
        seen = set()
        for col in range(len(board[0])):
            if board[row][col] in seen:
                return False
            if board[row][col] != '.':
                seen.add(board[row][col])
                if board[row][col] in boxes[row//3][col//3]:
                    return False
                boxes[row//3][col//3].add(board[row][col])
        
    #loop through all cloumns to make sure our contraints aren't violated
    for col in range(len(board[0])):
        seen = set()
        for row in range(len(board)):
            if board[row][col] in seen:
                return False
            if board[row][col] != '.':
                seen.add(board[row][col])
    return True

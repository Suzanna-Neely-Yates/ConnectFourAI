# Suzanna (Neely) Yates
# 
# Class: Board
#   -- Variable: Data storing the two-dimensional array (LoL), which is the game board.
#   -- Variable: Height storing the number of rows on the game board.
#   -- Variable: Width storing the number of columns on the game board.
#
# Data Members: Two-Dimensional List (LoL)
#  -- contains charactures to represent the game area
#  -- pair of variables holding the number of rows and columns on the board (6 rows and 7 columns - standard)

import random

"""
Inarow functions outside the class.
"""

def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # out of bounds col
    
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # out of bounds col

    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # out of bounds

    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # out of bounds col

    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # bottom of the board

        s += '\n' # and the numbers underneath here

        for col in range(0, self.width):
            s += " " + str(col%10)

        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """
        Inputs self, col and ox.
        Outputs the adding of the move. Placing it on the board.
        """
        H = self.height
        for row in range(0,H):
            if self.data[row][col] != " ":
                self.data[row-1][col] = ox  
                return
        self.data[H-1][col] = ox
    
    def clear(self):
        """
        Inputs self.
        Outputs the cleared chart.
        """
        H = self.height
        W = self.width
        for row in range(0, H):
            for col in range(0, W):
                self.data[row][col] = " "
        return

    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call board.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or board.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def allowsMove (self, col):
        """
        True if col is in-bounds and open.
        False otherwise.
        """
        H = self.height
        W = self.width
        D = self.data
        if col >= W or col < 0:
            return False
        elif D[0][col] != " ":
            return False
        else:
            return True

    def isFull(self):
        """
        Inputs self and outputs if the chart is full: 
        True or False.
        """
        H = self.height
        W = self.width
        D = self.data
        for col in range(W):
            if D[0][col]== " ":
                return False
        return True
        
    def delMove(self, col):
        """
        Inputs self and col.
        Outputs a deleted move.
        """
        H = self.height
        for row in range(0,H):
            if self.data[row][col] != " ":
                self.data[row][col] = " "  
                return


    def winsFor(self, ox):
        """
        Inputs self and ox.
        Outputs if ox wins.
        """
        H = self.height
        W = self.width
        D = self.data
        for row in range(H):
            for col in range(W):
                if inarow_Neast(ox, row, col, self.data, 4) == True:
                    return True
                if inarow_Nsouth(ox, row, col, self.data, 4) == True:
                    return True 
                if inarow_Nnortheast(ox, row, col, self.data, 4) == True:
                    return True
                if inarow_Nsoutheast(ox, row, col, self.data, 4) == True:
                    return True
        else:
            return False

    def hostGame(self):
        """
        Inputs self.
        Outputs the game a user can play.
        """
        print ("Welcome to Connect Four!") 
        width = self.width
        height = self.height   
        #board = Board(width, height)
        print (self)
        playing = True
        while playing == True:
            xusers_col = -1
            while not self.allowsMove(xusers_col):
                xusers_col = int(input("X, choose a column: "))
            self.addMove(xusers_col, "X")
            print(self)
            if self.winsFor("X") == True:
                print ("Congrats. You won!")
                playing = False
                break
            elif self.isFull() == True:
                print ("Board is full.")
                playing = False
                break

            ousers_col = -1
            while not self.allowsMove(ousers_col):
                choice = self.aiMove("O")
                ousers_col = choice #int(input("O, choose a column: "))
            self.addMove(ousers_col, "O")
            print(self)
            if self.winsFor("O") == True:
                print ("Congrats. You won!")
                playing = False
                break
            elif self.isFull() == True:
                print ("Board is full.")
                playing = False
                break

    def colsToWin(self, ox):
        """
        Inputs self, ox.
        Outputs a list of columns where the player can win.
        """
        list_wins = []
        for a in range(self.width): #column in board
            if self.allowsMove(a) == True:
                trial = self.addMove(a, ox) 
                if self.winsFor(ox) == True:
                    list_wins.append(a)
            self.delMove(a)
        return list_wins #return list of columns where ox move to win

    def aiMove(self, ox):
        """
        Inputs o or x.
        Outputs the column the computer chooses.
        """
        list_wins = self.colsToWin(ox)
        switch = self.switchatob(ox)
        list_lose = self.colsToWin(switch)
        if len(list_wins) != 0: #if computer can win
            return list_wins[0]
            #self.addMove(list_wins[0], ox)
        elif len(list_lose) != 0: #if computer cannot win
            return list_lose[0]
            #self.addMove(list_lose[0], ox )#block opponent
        else: #if no way for ox to win nor way to block ox
            random_move = random.randrange(self.width)
            while not self.allowsMove(random_move):
                random_move = random.randrange(self.width)
            return random_move
            #self.addMove(random_move, ox)

    def switchatob (self, ox):
        """
        Helper function for aiMove.
        Inputs x or o.
        Outputs the opposite letter.
        """
        if ox == "X" or ox == "x":
            return "O"
        elif ox == "O" or ox == "o":
            return "X"
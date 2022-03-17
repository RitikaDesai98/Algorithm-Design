#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math

def solveBoard(board, row, rowmask,ldmask, rdmask):
    n = len(board)

    all_rows_filled = (1 << n) - 1

    if (rowmask == all_rows_filled):
        global ways
        ways = ways + 1

    safe = all_rows_filled & (~(rowmask | ldmask | rdmask))

    while (safe > 0):

        p = safe & (-safe)
        col = (int)(math.log(p) / math.log(2))
        board[row][col] = 'Q'
        solveBoard(board, row + 1, rowmask | p, (ldmask | p) << 1, (rdmask | p) >> 1)
        safe = safe & (safe - 1)
        board[row][col] = ' '

def createBoard(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(' ')
        board.append(row)
    return board

def main():

    n = 4
    board = createBoard(n)
    rowmask = 0
    ldmask = 0
    rdmask = 0
    row = 0
    global ways
    ways = 0
    solveBoard(board, row, rowmask, ldmask, rdmask)
    print("Number of ways to place " + (str)(n) + " queens : " + (str)(ways))


    n = 8
    board = createBoard(n)
    rowmask = 0
    ldmask = 0
    rdmask = 0
    row = 0
    ways = 0
    solveBoard(board, row, rowmask, ldmask, rdmask)
    print("Number of ways to place " + (str)(n) + " queens : " + (str)(ways))

    n = 10
    board = createBoard(n)
    rowmask = 0
    ldmask = 0
    rdmask = 0
    row = 0
    ways = 0
    solveBoard(board, row, rowmask, ldmask, rdmask)
    print("Number of ways to place " + (str)(n) + " queens : " + (str)(ways))

    n = 12
    board = createBoard(n)
    rowmask = 0
    ldmask = 0
    rdmask = 0
    row = 0
    ways = 0
    solveBoard(board, row, rowmask, ldmask, rdmask)
    print("Number of ways to place " + (str)(n) + " queens : " + (str)(ways))


if __name__ == "__main__":
    main()


# In[ ]:





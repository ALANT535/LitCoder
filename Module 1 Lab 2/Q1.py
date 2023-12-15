import sys

def is_valid(l):
    
    visited = []
    for j in l:
        if (j in visited and j!="."):
            #print(l,"\tError is in ",j)
            return False
            
        else:
            visited.append(j)
    return True

def doSomething(inval):
    
    #3 conditions
    
    #1 for rows
    for i in board:
        if (not is_valid(i)):
            return False
            
    
    #2 for columns
    col_counter = 0
    while (col_counter<9):
        l = []
        for i in board:
            k = i[col_counter]
            l.append(k)
        
        if (not is_valid(l)):
            return False
        col_counter+= 1

    #3 for boxes
    
    l = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    
    for i in l:
        temp_l = []
        row1 = i[0]
        col1 = i[1]
        temp_l = board[row1][col1:col1+3] + board[row1+1][col1:col1+3] + board[row1+2][col1:col1+3]
        
        if (not is_valid(temp_l)):
            return False
 
    return True
  
inputVal = int(input())
board = []
for i in range(inputVal):
    board.append(input().split())
    
outputVal = doSomething(board)
print (outputVal)

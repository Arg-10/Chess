#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Making the board
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
rows = ['1', '2', '3', '4', '5', '6', '7', '8']
board = []
for r in rows:
    grid = [str (c) + str (r) for c in columns]           # Defining the grid
    board.append (grid)                                # Adding the grids to board
    
# Finding possible moves of the King
def king_moves (loc, colour):
    c = list (loc) [0]          
    cl = columns.index (c)        
    r = list (loc) [1]
    rw = rows.index (r)                 # Converting the inputs to list indices
    col, row = 0, 0
    move = []
    for i in range (-1, 2):             
        for j in range (-1, 2):         # Considering all possible ranges of grids
            col = cl + i
            row = rw + j
            if col >= 0 and col <= 7 and row >= 0 and row <= 7:     # Ensuring the grid is within the board
                cell = str (col) + str (row)
                move.append (cell)      # Making a list with possible moves represented with list indices joined together
    move.remove (str (cl) + str (rw))
    moves = []
    for i in move:
        mv = board [int (list (i) [1])] [int (list (i) [0])]   # Finding the associated grids for possible moves
        moves.append (mv)
    return ([moves, colour])


# In[2]:

# Finding possible moves of the Bishop
def bishop_moves (loc, colour):
    c = list (loc) [0]          
    cl = columns.index (c)        
    r = list (loc) [1]
    rw = rows.index (r)                 # Converting the inputs to list indices
    col, row = 0, 0
    move = []
    for i in range (-7, 8):    
        for j in range (-7, 8): 
            if abs (i) == abs (j):     # Considering all possible ranges of grids
                col = cl + i
                row = rw + j
                if col >= 0 and col <= 7 and row >= 0 and row <= 7:     # Ensuring the grid is within the board
                    cell = str (col) + str (row)
                    move.append (cell)      # Making a list with possible moves represented with list indices joined together
    move.remove (str (cl) + str (rw))
    moves = []
    for i in move:
        mv = board [int (list (i) [1])] [int (list (i) [0])]   # Finding the associated grids for possible moves
        moves.append (mv)
    return ([moves, colour])


# In[3]:
    
# Finding possible moves of the Rook
def rook_moves (loc, colour):
    c = list (loc) [0]          
    cl = columns.index (c)        
    r = list (loc) [1]
    rw = rows.index (r)                 # Converting the inputs to list indices
    col, row = 0, 0
    move = []
    for i in range (-7, 8):             
        for j in range (-7, 8):         # Considering all possible ranges of grids
            if abs (i) != abs (j):
                col = cl + i
                row = rw + j
                if col >= 0 and col <= 7 and row >= 0 and row <= 7:     # Ensuring the grid is within the board
                    if col == cl or row == rw:
                        cell = str (col) + str (row)
                        move.append (cell)      # Making a list with possible moves represented with list indices joined together
    moves = []
    for i in move:
        mv = board [int (list (i) [1])] [int (list (i) [0])]   # Finding the associated grids for possible moves
        moves.append (mv)
    return ([moves, colour])


# In[4]:

# Finding possible moves of the Queen
def queen_moves (loc, colour):
    c = list (loc) [0]          
    cl = columns.index (c)        
    r = list (loc) [1]
    rw = rows.index (r)                 # Converting the inputs to list indices
    col, row = 0, 0
    move = []
    for i in range (-7, 8):             
        for j in range (-7, 8):         # Considering all possible ranges of grids
            if abs (i) != abs (j):
                col = cl + i
                row = rw + j
                if col >= 0 and col <= 7 and row >= 0 and row <= 7:     # Ensuring the grid is within the board
                    if col == cl or row == rw:
                        cell = str (col) + str (row)
                        move.append (cell)      # Making a list with possible moves represented with list indices joined together
            elif abs (i) == abs (j):     # Considering all possible ranges of grids
                col = cl + i
                row = rw + j
                if col >= 0 and col <= 7 and row >= 0 and row <= 7:     # Ensuring the grid is within the board
                    cell = str (col) + str (row)
                    move.append (cell)      # Making a list with possible moves represented with list indices joined together
    move.remove (str (cl) + str (rw))
    moves = []
    for i in move:
        mv = board [int (list (i) [1])] [int (list (i) [0])]   # Finding the associated grids for possible moves
        moves.append (mv)
    return ([moves, colour])


# In[5]:
    
# Finding possible moves of the Knight
def knight_moves (loc, colour):
    c = list (loc) [0]          
    cl = columns.index (c)        
    r = list (loc) [1]
    rw = rows.index (r)                 # Converting the inputs to list indices
    col, row = 0, 0
    move = []
    for i in range (-2, 3, 4):    
        for j in range (-1, 2, 2):      # Considering all possible ranges of grids
                col = cl + i
                row = rw + j
                if col >= 0 and col <= 7 and row >= 0 and row <= 7:     # Ensuring the grid is within the board
                    cell1 = str (col) + str (row)
                    move.append (cell1)      # Making a list with possible moves represented with list indices joined together 
    for i in range (-2, 3, 4):    
        for j in range (-1, 2, 2):      # Considering all possible ranges of grids
                col = cl + j
                row = rw + i
                if col >= 0 and col <= 7 and row >= 0 and row <= 7:     # Ensuring the grid is within the board
                    cell2 = str (col) + str (row)
                    move.append (cell2)
    #move.remove (str (cl) + str (rw))
    moves = []
    for i in move:
        mv = board [int (list (i) [1])] [int (list (i) [0])]   # Finding the associated grids for possible moves
        moves.append (mv)
    return ([moves, colour])


# In[6]:

# Finding possible moves of the Pawn
def pawn_moves (loc, colour):
    c = list (loc) [0]          
    cl = columns.index (c)        
    r = list (loc) [1]
    rw = rows.index (r)                 # Converting the inputs to list indices
    col, row = 0, 0
    move = []
    if colour == "W":
        if rw == 1:
            for i in range (1, 3):
                row = rw + i
                cell3 = str (cl) + str (row)
                move.append (cell3)      # Making a list with possible moves represented with list indices joined together
        else:
            row = rw + 1
            if row >= 0 and row <= 7:   # Ensuring the grid is within the board
                cell4 = str (cl) + str (row)
                move.append (cell4)      # Making a list with possible moves represented with list indices joined together
    elif colour == "B":
        if rw == 6:
            for i in range (1, 3):
                row = rw - i
                cell1 = str (cl) + str (row)
                move.append (cell1)      # Making a list with possible moves represented with list indices joined together
        else:
            row = rw - 1
            if row >= 0 and row <= 7:   # Ensuring the grid is within the board
                cell2 = str (cl) + str (row)
                move.append (cell2)      # Making a list with possible moves represented with list indices joined
    moves = []
    for i in move:
        mv = board [int (list (i) [1])] [int (list (i) [0])]   # Finding the associated grids for possible moves
        moves.append (mv)
    return ([moves, colour])


# In[7]:


# Possible moves of the pieces
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
rows = ['1', '2', '3', '4', '5', '6', '7', '8']
#loc_k = input ('Enter the position of the King: ')
#loc_b = input ('Enter the position of the Bishop: ')
#loc_r = input ('Enter the position of the Rook: ')
#loc_q = input ('Enter the position of the Queen: ')
#loc_p = input ('Enter the position of the Pawn: ')
#loc_n = input ('Enter the position of the Knight: ')
#col_k = input ('Enter the colour of the King: ')
#col_b = input ('Enter the colour of the Bishop: ')
#col_r = input ('Enter the colour of the Rook: ')
#col_q = input ('Enter the colour of the Queen: ')
#col_p = input ('Enter the colour of the Pawn: ')
#col_n = input ('Enter the colour of the Knight: ')
loc_k, loc_b, loc_r, loc_q, loc_p, loc_n = 'E4', 'H3', 'E2', 'E7', 'G4', 'D5'
col_k, col_b, col_r, col_q, col_p, col_n = 'B', 'B', 'W', 'B', 'W', 'W'
loc_list = [loc_k, loc_b, loc_r, loc_q, loc_p, loc_n]
k_m, b_m, r_m, q_m, p_m, n_m = king_moves (loc_k, col_k) [0], bishop_moves (loc_b, col_b) [0], rook_moves (loc_r, col_r) [0], queen_moves (loc_q, col_q) [0], pawn_moves (loc_p, col_p) [0], knight_moves (loc_n, col_n) [0]
col_list = [col_k, col_b, col_r, col_q, col_p, col_n]
moves_list = [k_m, b_m, r_m, q_m, p_m, n_m]
pieces_list = ['King', 'Bishop', 'Rook', 'Queen', 'Pawn', 'Knight']

# Eliminating the possible moves beyond an obstacle
k_m1 = [i for i in k_m]     

b_m1 = [i for i in b_m]
for j in loc_list:
    if b_m.count (j) > 0:
        for k in b_m1:
            if columns.index (j [0]) < columns.index (loc_b [0]) and j [1] > loc_b [1] and columns.index (k [0]) < columns.index (j [0]) and k [1] > j [1]:
                b_m1.remove (k)
for j in loc_list:
    if b_m.count (j) > 0:
        for k in b_m1:
            if columns.index (j [0]) > columns.index (loc_b [0]) and j [1] > loc_b [1] and columns.index (k [0]) > columns.index (j [0]) and k [1] > j [1]:
                b_m1.remove (k)
for j in loc_list:
    if b_m.count (j) > 0:
        for k in b_m1:
            if columns.index (j [0]) < columns.index (loc_b [0]) and j [1] > loc_b [1] and columns.index (k [0]) < columns.index (j [0]) and k [1] > j [1]:
                b_m1.remove (k)
for j in loc_list:
    if b_m.count (j) > 0:
        for k in b_m1:
            if columns.index (j [0]) > columns.index (loc_b [0]) and j [1] < loc_b [1] and columns.index (k [0]) > columns.index (j [0]) and k [1] < j [1]:
                b_m1.remove (k)
for j in loc_list:
    if b_m.count (j) > 0:
        for k in b_m1:
            if columns.index (j [0]) < columns.index (loc_b [0]) and j [1] < loc_b [1] and columns.index (k [0]) < columns.index (j [0]) and k [1] < j [1]:
                    b_m1.remove (k)
for j in loc_list:
    if b_m.count (j) > 0:
        for k in b_m1:
            if columns.index (j [0]) > columns.index (loc_b [0]) and j [1] < loc_b [1] and columns.index (k [0]) > columns.index (j [0]) and k [1] < j [1]:
                b_m1.remove (k)
for j in loc_list:
    if b_m.count (j) > 0:
        for k in b_m1:
            if columns.index (j [0]) < columns.index (loc_b [0]) and j [1] < loc_b [1] and columns.index (k [0]) < columns.index (j [0]) and k [1] < j [1]:
                    b_m1.remove (k)
                        
r_m1 = [i for i in r_m]
for j in loc_list:
    if r_m.count (j) > 0:
        for i in r_m1:
            if j [1] > loc_r [1]:
                if i [1] > j [1]:
                    r_m1.remove (i)
for j in loc_list:
    if r_m.count (j) > 0:
        for i in r_m1:
            if columns.index (j [0]) < columns.index (loc_r [0]):
                if columns.index (i [0]) < columns.index (j [0]):
                    r_m1.remove (i)
for j in loc_list:
    if r_m.count (j) > 0:
        for i in r_m1:
            if columns.index (j [0]) > columns.index (loc_r [0]):
                if columns.index (i [0]) > columns.index (j [0]):
                    r_m1.remove (i)
for j in loc_list:
    if r_m.count (j) > 0:
        for i in r_m1:
            if columns.index (j [0]) > columns.index (loc_r [0]):
                if columns.index (i [0]) > columns.index (j [0]):
                    r_m1.remove (i)
for j in loc_list:
    if r_m.count (j) > 0:
        for i in r_m1:
            if j [1] < loc_r [1]:
                if i [1] < j [1]:
                    r_m1.remove (i)
for j in loc_list:
    if r_m.count (j) > 0:
        for i in r_m1:
            if columns.index (j [0]) < columns.index (loc_r [0]):
                if columns.index (i [0]) < columns.index (j [0]):
                    r_m1.remove (i)
for j in loc_list:
    if r_m.count (j) > 0:
        for i in r_m1:
            if j [1] > loc_r [1]:
                if i [1] > j [1]:
                    r_m1.remove (i)
for j in loc_list:
    if r_m.count (j) > 0:
        for i in r_m1:
            if j [1] < loc_r [1]:
                if i [1] < j [1]:
                    r_m1.remove (i)
            
q_m1 = [i for i in q_m]
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) > columns.index (loc_q [0]) and j [1] == loc_q [1]:
                if columns.index (i [0]) > columns.index (j [0]) and i [1] == j [1]:
                    q_m1.remove (i)
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) == columns.index (loc_q [0]) and j [1] < loc_q [1]:
                if columns.index (i [0]) == columns.index (j [0]) and i [1] < j [1]:
                    q_m1.remove (i)
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) < columns.index (loc_q [0]) and j [1] == loc_q [1]:
                if columns.index (i [0]) < columns.index (j [0]) and i [1] == j [1]:
                    q_m1.remove (i)
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) == columns.index (loc_q [0]) and j [1] > loc_q [1]:
                if columns.index (i [0]) == columns.index (j [0]) and i [1] > j [1]:
                    q_m1.remove (i)
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) > columns.index (loc_q [0]) and j [1] < loc_q [1]:
                if columns.index (i [0]) > columns.index (j [0]) and i [1] < j [1]:
                    q_m1.remove (i)
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) == columns.index (loc_q [0]) and j [1] < loc_q [1]:
                if columns.index (i [0]) == columns.index (j [0]) and i [1] < j [1]:
                    q_m1.remove (i)
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) > columns.index (loc_q [0]) and j [1] == loc_q [1]:
                if columns.index (i [0]) > columns.index (j [0]) and i [1] == j [1]:
                    q_m1.remove (i)
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) < columns.index (loc_q [0]) and j [1] < loc_q [1]:
                if columns.index (i [0]) < columns.index (j [0]) and i [1] < j [1]:
                    q_m1.remove (i)
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) < columns.index (loc_q [0]) and j [1] == loc_q [1]:
                if columns.index (i [0]) < columns.index (j [0]) and i [1] == j [1]:
                    q_m1.remove (i)
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) == columns.index (loc_q [0]) and j [1] > loc_q [1]:
                if columns.index (i [0]) == columns.index (j [0]) and i [1] > j [1]:
                    q_m1.remove (i)
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) == columns.index (loc_q [0]) and j [1] < loc_q [1]:
                if columns.index (i [0]) == columns.index (j [0]) and i [1] < j [1]:
                    q_m1.remove (i)
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) > columns.index (loc_q [0]) and j [1] > loc_q [1]:
                if columns.index (i [0]) > columns.index (j [0]) and i [1] > j [1]:
                    q_m1.remove (i)
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) > columns.index (loc_q [0]) and j [1] < loc_q [1]:
                if columns.index (i [0]) > columns.index (j [0]) and i [1] < j [1]:
                    q_m1.remove (i)
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) < columns.index (loc_q [0]) and j [1] > loc_q [1]:
                if columns.index (i [0]) < columns.index (j [0]) and i [1] > j [1]:
                    q_m1.remove (i)
for j in loc_list:
    if q_m.count (j) > 0:
        for i in q_m1:
            if columns.index (j [0]) < columns.index (loc_q [0]) and j [1] < loc_q [1]:
                if columns.index (i [0]) < columns.index (j [0]) and i [1] < j [1]:
                    q_m1.remove (i)
                        
p_m1 = [i for i in p_m]
for j in loc_list:
    if p_m.count (j) > 0:
        for i in p_m1:
            if int (list (j) [1]) > int (list (loc_p) [1]):
                if (list (i)) [1] > (list(j)) [1]:
                    p_m1.remove (i)
    if pawn_moves (loc_p, col_p) [1] == 'W':
        if columns.index (list (j) [0]) - columns.index (list (loc_p) [0]) == 1 and int (list (j) [1]) - int (list (loc_p) [1]) == 1:
            p_m1.append (j)
        if columns.index (list (j) [0]) - columns.index (list (loc_p) [0]) == -1 and int (list (j) [1]) - int (list (loc_p) [1]) == 1:
            p_m1.append (j)
    elif pawn_moves (loc_p, col_p) [1] == 'B':
        if columns.index (list (j) [0]) - columns.index (list (loc_p) [0]) == 1 and int (list (j) [1]) - int (list (loc_p) [1]) == -1:
            p_m1.append (j)
        if columns.index (list (j) [0]) - columns.index (list (loc_p) [0]) == -1 and int (list (j) [1]) - int (list (loc_p) [1]) == -1:
            p_m1.append (j)
            
n_m = [i for i in n_m]

moves_list_D = [k_m1, b_m1, r_m1, q_m1, p_m1, n_m]
import copy
moves_lists = copy.deepcopy (moves_list_D)    # Creating an independent copy of the list for future use

# Eliminating the grids occupied by same colour pieces from list of possible moves
for i in range (len (col_list)):
    for j in range (len (col_list)):
        if i != j:
            if col_list [i] == col_list [j]:
                if i == 4:      # Applying special rule for pawn due to its unusual coup movements
                    if moves_list_D [i].count (loc_list [j]) > 0:   
                        moves_list_D [i].remove (loc_list [j])
                else:
                    if moves_list [i].count (loc_list [j]) > 0:
                        if moves_list_D [i].count (loc_list [j]) > 0:
                            moves_list_D [i].remove (loc_list [j])
            else:
                if i == 4:      # Applying special rule for pawn due to its unusual coup movements
                    if moves_list [i].count (loc_list [j]) > 0:
                        moves_list_D [i].remove (loc_list [j])

moves_list_f = [k_m1, b_m1, r_m1, q_m1, p_m1, n_m]
# Eliminating possible checks from the list of possible moves of the King
for i in range (len (moves_list_f)):
    for j in range (len (moves_list_f)):
        if col_list [i] != col_list [j]:
            for k in moves_list_f [i]:
                if i == 0:
                    if j == 4:
                        if pawn_moves (loc_p, col_p) [1] == 'W':
                            if columns.index (k [0]) - columns.index (loc_list [j] [0]) == 1 and int (k [1]) - int (loc_list [j] [1]) == 1:
                                k_m1.remove (k)
                            elif columns.index (k [0]) - columns.index (loc_list [j] [0]) == -1 and int (k [1]) - int (loc_list [j] [1]) == 1:
                                k_m1.remove (k)
                        if pawn_moves (loc_p, col_p) [1] == 'B':
                            if columns.index (k [0]) - columns.index (loc_list [j] [0]) == 1 and int (k [1]) - int (loc_list [j] [1]) == -1:
                                k_m1.remove (k)
                            elif columns.index (k [0]) - columns.index (loc_list [j] [0]) == -1 and int (k [1]) - int (loc_list [j] [1]) == -1:
                                k_m1.remove (k)
                    else:
                        if moves_lists [j].count (k) > 0:
                            k_m1.remove (k)

# Display check and checkmate at the current position
for i in range (len (moves_list_f)):
    if col_k != col_list [i]:
        if moves_list_f [i].count (loc_k) > 0:
            if len (moves_list_f [0]) != 0:
                print ("The %s King is at check by %s!" % (col_list [i],pieces_list [i]))
            else:
                print ("It's a checkmate on the %s King!" % col_list [0])
            
print ('Possible moves of the %s King:' % (col_list [0]), k_m1)
print ('Possible moves of the %s Bishop:' % (col_list [1]), b_m1)
print ('Possible moves of the %s Rook:' % (col_list [2]), r_m1)
print ('Possible moves of the %s Queen:' % (col_list [3]), q_m1)
print ('Possible moves of the %s Pawn:' % (col_list [4]), p_m1)
print ('Possible moves of the %s Knight:' % (col_list [5]), n_m)

# Displaying the possible coups a piece can make from its current position
moves_list_f = [k_m1, b_m1, r_m1, q_m1, p_m1, n_m]
for i in range (len (moves_list_f)):
    for j in range (len (loc_list)):
        if moves_list_f [i].count (loc_list [j]) > 0:
            if j != 0:
                print ("The %s %s can coup the %s %s from current position!" % (col_list [i], pieces_list  [i], col_list [j], pieces_list [j]))
# Displaying the possible coups at different possible moves of the pieces
for i in range (len (moves_list_f)):
    for j in range (len (moves_list_f)):
        if col_list [i] != col_list [j]:
            for k in moves_list_f [i]:
                if moves_lists [j].count (k) > 0:
                    if i != 0:
                        if j != 0:
                            print ("Possible coup of the %s %s by the %s %s at position %s" % (col_list [i], pieces_list  [i], col_list [j], pieces_list [j], k))
                        else:
                            if moves_list_f [j].count (k) > 0:
                                print ("Possible coup of %s by %s at position %s" % (col_list [i], pieces_list  [i], col_list [j], pieces_list [j], k))                                        





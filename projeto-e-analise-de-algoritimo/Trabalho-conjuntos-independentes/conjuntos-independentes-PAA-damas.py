import networkx as nx
import itertools 

numCells = 6

# create a matrix of the board nxn
def create_board(numCells):
    board = []
    for i in range(numCells):
        board.append([])
        for j in range(numCells):
            board[i].append('X')
    return board

# print the board on the chess format
def print_board(board):
    print("Board:")
    for i in range(len(board[0])):
        for j in range(len(board)):
            print(board[j][i], end='  ')
        print('\n', end='')
        

def clean_board(board):
    for i in range(len(board[0])):
        for j in range(len(board)):
            board[j][i] = 'X'
    return board
        
chessBoard = create_board(numCells)
print_board(chessBoard)

# create a graph for represent the chess board n x n
cellsBoard = numCells
board = nx.Graph()
for i in range(cellsBoard):
    for j in range(cellsBoard):
        board.add_node((i,j))

# add edges between the nodes in the horizontal, vertical and horizontal range
# this algorithm is not clean because is making a edge between node a and node b and other edge between node b and node a

for i in range(cellsBoard):
    for j in range(cellsBoard):
        for k in range(cellsBoard):
            # making the horizontal edges
            if j != k:
                board.add_edge((i, j), (i, k))
            # making the vertical edges
            if i != k:
                board.add_edge((i, j), (k, j))
        # making the horizontal range edges
        # illustration of the diagonals: https://drive.google.com/file/d/1xdbqjWrVbb79z2TbClz5LRUDkT3foabf/view?usp=sharing
        for k in range(1, cellsBoard):
            if (i - k) >= 0 and (j - k) >= 0:
                board.add_edge((i, j), (i - k, j - k))
            if (i + k) < cellsBoard and (j + k) < cellsBoard:
                board.add_edge((i, j), (i + k, j + k))
            if (i + k) < cellsBoard and (j - k) >= 0:
                board.add_edge((i, j), (i + k, j - k))
            if (i - k) >= 0 and (j + k) < cellsBoard:
                board.add_edge((i, j), (i - k, j + k))                

# choose a node and verify if has a edge with the other nodes
candidatesSets = []
queensOnBoard = []
accept = True

for i in range(1, numCells + 1):
    candidatesSets += itertools.combinations(board.nodes(), i)

independentSets = []
approvedSet = True
control1 = 0
for candidate in candidatesSets:
    control1 = 0
    for node1 in range(control1, len(candidate)):
        control2 = 0
        for node2 in range(control2, len(candidate)):
            if candidate[node1] != candidate[node2]:
                if board.has_edge(candidate[node1], candidate[node2]):
                    approvedSet = False
                    break
        if not approvedSet:
            break
        control2 += 1
    if approvedSet:
        independentSets.append(candidate)
    approvedSet = True
    control1 += 1

print('Independent sets: ', independentSets)
                
# selecting the maximal sets
maximalSets = []
maxlength = 0
for i in independentSets:
    if len(i) > maxlength:
        maximalSets = []
        maximalSets.append(i)
        maxlength = len(i)
    elif len(i) == maxlength:
        maximalSets.append(i)
        
print('Maximal sets: ', maximalSets)

for sets in maximalSets:
    clean_board(chessBoard)
    for i, j in sets:
        chessBoard[i][j] = 'Q'    
    print_board(chessBoard)
    print('Queens: ', sets)

print(len(maximalSets))
    
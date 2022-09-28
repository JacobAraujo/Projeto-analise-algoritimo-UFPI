import networkx as nx

numCells = 50

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
        
chessBoard = create_board(numCells)
#print_board(chessBoard)

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

def normalStrategy(board, queensOnBoard):
    newQueen = True
    for boardNode in board.nodes():
        for queen in queensOnBoard:
            if board.has_edge(queen, boardNode):
                newQueen = False
                break
        if newQueen:
            queensOnBoard += [boardNode]
        newQueen = True
    return queensOnBoard

def furtherStrategy(board, queensOnBoard):
    newQueen = True
    isBelow = True
    for i in range(numCells):
        if isBelow:
            for j in range(numCells):
                for queen in queensOnBoard:
                    if board.has_edge(queen, (i, j)):
                        newQueen = False
                        break
                if newQueen:
                    queensOnBoard += [(i, j)]
                    isBelow = j >= numCells/2
                    break
                newQueen = True
        else:
            for j in range(numCells - 1, -1, -1):
                for queen in queensOnBoard:
                    if board.has_edge(queen, (i, j)):
                        newQueen = False
                        break
                if newQueen:
                    queensOnBoard += [(i, j)]
                    isBelow = j >= numCells/2
                    break
                newQueen = True
    return queensOnBoard                

#queensOnBoard = normalStrategy(board, queensOnBoard)
queensOnBoard = furtherStrategy(board, queensOnBoard)

for i, j in queensOnBoard:
    chessBoard[i][j] = 'Q'        

print('Queens: ')
print(queensOnBoard)
print('Expect number of queens: ', numCells)
print('Number of queens: ', len(queensOnBoard))

    
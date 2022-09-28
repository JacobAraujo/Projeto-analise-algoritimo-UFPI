import networkx as nx
import pandas as pd

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
        
# add edges between the nodes in the horizontal, vertical and horizontal range
# this algorithm is not clean because is making a edge between node a and node b and other edge between node b and node a

def makeGraphBoard(numCells):
    board = nx.Graph()
    for i in range(numCells):
        for j in range(numCells):
            board.add_node((i,j))
    for i in range(numCells):
        for j in range(numCells):
            for k in range(numCells):
                # making the horizontal edges
                if j != k:
                    board.add_edge((i, j), (i, k))
                # making the vertical edges
                if i != k:
                    board.add_edge((i, j), (k, j))
            # making the horizontal range edges
            # illustration of the diagonals: https://drive.google.com/file/d/1xdbqjWrVbb79z2TbClz5LRUDkT3foabf/view?usp=sharing
            for k in range(1, numCells):
                if (i - k) >= 0 and (j - k) >= 0:
                    board.add_edge((i, j), (i - k, j - k))
                if (i + k) < numCells and (j + k) < numCells:
                    board.add_edge((i, j), (i + k, j + k))
                if (i + k) < numCells and (j - k) >= 0:
                    board.add_edge((i, j), (i + k, j - k))
                if (i - k) >= 0 and (j + k) < numCells:
                    board.add_edge((i, j), (i - k, j + k))
    return board                

def normalStrategy(board, queensOnBoard, numCells):
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


# retirar numCells de argumentos
def furtherStrategy(board, queensOnBoard, numCells):
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


def main():
    
    strategy_data = pd.DataFrame({"normal": [], "further": []})
    print(strategy_data)
    for numCells in range(150):
        board = makeGraphBoard(numCells)

        queensOnBoardNormal = []
        queensOnBoardFuther = []

        queensOnBoardNormal = normalStrategy(board, queensOnBoardNormal, numCells)
        queensOnBoardFuther = furtherStrategy(board, queensOnBoardFuther, numCells)
        
        numQueensNormal = len(queensOnBoardNormal)
        numQueensFuther = len(queensOnBoardFuther)
        
        strategy_data.loc[numCells] = [numQueensNormal, numQueensFuther]
    print(strategy_data)
    file_name = 'comparacao.xlsx'
    strategy_data.to_excel(file_name) 


main()
    

    #print('Queens: ')
    #print(queensOnBoard)
    #print(numCells, 'x', numCells)
    #print('Normal Strategy: ', len(queensOnBoardNormal))
    #print('Futher Strategy: ', len(queensOnBoardFuther))

    
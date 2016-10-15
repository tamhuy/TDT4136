import aStar
import djikstra
import BFS

boardtest = []
class Node:
    #A node class for initializing node objects
    g = None #Total traveled distance from start node
    f = float("inf") #Sets f to infinity so that we don't underestimate
    h = None #Heuristic for estimating distances
    w = None #Weight/ What it costs to travel to that node from an adjacent node
    char = None #what type of "terrain" it is (.#AB)
    parent = None #Parent of the node
    children = [] #Children of the node
    location = [] #Where on the map the node is located

    def __init__(self, y, x, c, w): #Initialize a node with coordinates, type of character and weight
        self.location = [y, x]
        self.char = c
        self.w = w

def loadBoard(filename): #Function to read from file
    f = open(filename, 'r')
    board = []
    tall = 0 #A number used to increment

    for line in f: #Goes through the txt file one line at a time
        board.append([]) #Elements in each line so it can be a 2-dimensional list
        for x in range(len(line)):
            if line[x] == '#': #Initilizes the walls whit a infinte weight
                board[tall].append(Node(tall, x, line[x], float("inf")))
            elif line[x] == 'w':
                board[tall].append(Node(tall, x, line[x], 100))
            elif line[x] == 'm':
                board[tall].append(Node(tall, x, line[x], 50))
            elif line[x] == 'f':
                board[tall].append(Node(tall, x, line[x], 10))
            elif line[x] == 'g':
                board[tall].append(Node(tall, x, line[x], 5))
            elif line[x] == 'r':
                board[tall].append(Node(tall, x, line[x], 1))
            else: #Initializes the rest of the nodes with weight 1
                board[tall].append(Node(tall, x, line[x], 1))

        del board[tall][-1] #Deletes the '\n'
        tall += 1

    f.close()
    return board


def findAB(board): #Function to find starting and ending point
    A = []
    B = []
    for i in range(len(board)):
        for j in range(len(board[i])): #Note i is for the y axis while j is for the x axis
            if board[i][j].char == 'A':
                A.append(i)
                A.append(j)
            if board[i][j].char == 'B':
                B.append(i)
                B.append(j)
    return A, B


def visualize(filename):  # Function to read from file
    f = open(filename, 'r')
    board = []
    tall = 0  # A number used to increment

    for line in f:  # Goes through the txt file one line at a time
        board.append([])  # Elements in each line so it can be a 2-dimensional list
        for x in range(len(line)):
            board[tall].append(line[x])

        del board[tall][-1]  # Deletes the '\n'
        tall += 1

    f.close()
    return board


def run():
    filename = "boards/board-2-4.txt"
    board = loadBoard(filename)
    A, B = findAB(board)
    open, closed = aStar.aStar(board, A, B)
    c = board[B[0]][B[1]]
    global boardtest
    boardtest = visualize(filename)
    #print boardtest

    for node in open:
        if node.char != 'A' and node.char != 'B':
            boardtest[node.location[0]][node.location[1]] = '*'

    for node in closed:
        if node.char != 'A' and node.char != 'B':
            boardtest[node.location[0]][node.location[1]] = 'x'

    while c.parent != None:
        c = c.parent
        if c.char != 'A':
            boardtest[c.location[0]][c.location[1]] = 'o'


    for line in boardtest:
        asd = ''
        for char in line:
            asd += str(char)
        print asd

run()

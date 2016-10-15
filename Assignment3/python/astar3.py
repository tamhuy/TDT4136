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


def heuristic(start, end): #Formula for Manhattan distance
    h = abs(start[0] - end[0]) + abs(start[1] - end[1])
    return h


def aStar(board): #Method for the A* algorithm
    closed, open = [], [] #Initialize open and closed as two lists
    A, B = findAB(board) #Finds the Start and end point in the board
    board[A[0]][A[1]].g = 0 #Sets the g, h and f values for the starting node
    board[A[0]][A[1]].h = heuristic(board[A[0]][A[1]].location, board[B[0]][B[1]].location)
    board[A[0]][A[1]].f = board[A[0]][A[1]].g + board[A[0]][A[1]].h
    open.append(board[A[0]][A[1]]) #Adds the starting node to the open list

    while True: #Agenda loop
        if len(open) == 0:# If the goal cannot be reached, return fail
            return False
        x = open.pop() #take the top element of the open stack and place it in the closed stack
        closed.append(x)
        #print x.location #used to see which nodes the algorithm visits
        #print x.f #Used to see the f distance for the current node
        if x.location == B:# if you have arrived at the end position then end
            return True
        children = []

        #The four next if-sentences are for determining if you are on the edge of the board or if the node you want to check is a wall
        if x.location[0] != 0:
            if board[x.location[0]-1][x.location[1]].char != '#':
                children.append(board[x.location[0]-1][x.location[1]])

        if x.location[0] != len(board)-1:
            if board[x.location[0]+1][x.location[1]].char != '#':
                children.append(board[x.location[0]+1][x.location[1]])

        if x.location[1] != 0:
            if board[x.location[0]][x.location[1] - 1].char != '#':
                children.append(board[x.location[0]][x.location[1] - 1])

        if x.location[1] != len(board[0])-1:
            if board[x.location[0]][x.location[1]+1].char != '#':
                children.append(board[x.location[0]][x.location[1]+1])

        #For each successors to the current node
        for i in children:
            x.children.append(i) #Add the children to the current node

            if i not in open and i not in closed: #The following lines are used to attach the child to the parent and evaluate if the current f distance is shorter or if there is a shorter one
                attachAndEval(i, x, B)
                open.append(i)
            elif x.g + i.w < i.g:
                attachAndEval(i, x, B)

        open.sort(key=lambda q: q.f, reverse = True) #Lambda function so sort the open list


def attachAndEval(node,parent, B):
    node.parent = parent
    node.g = parent.g + node.w
    node.h = heuristic(node.location, B)
    node.f = node.g + node.h


def propagate(P):
    for c in P.children:
        if P.g + c.w < c.g:
            c.parent = P
            c.g = g
            c.f = c.g + c.h
            propagate(c)



def loadBoard2(filename): #Function to read from file
    f = open(filename, 'r')
    board = []
    tall = 0 #A number used to increment

    for line in f: #Goes through the txt file one line at a time
        board.append([]) #Elements in each line so it can be a 2-dimensional list
        for x in range(len(line)):
            board[tall].append(line[x])

        del board[tall][-1] #Deletes the '\n'
        tall += 1

    f.close()
    return board


board = loadBoard("boards/board-2-1.txt")
aStar(board)
A, B = findAB(board)
c = board[B[0]][B[1]]

board2 = loadBoard2("boards/board-1-1.txt")


def visualize():
    while c.parent != None:
        print c.parent.location
        board2[c.location[0]][c.location[1]] = 'X'
        c = c.parent

    for line in board2:
        print line
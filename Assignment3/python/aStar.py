#The A* algorithm is based on the sudo code provided in the "Supplement - Essentials of the AStas Algorithm.pdf" included with the assignment
def aStar(board,A,B): #Method for the A* algorithm
    closed, open = [], [] #Initialize open and closed as two lists
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

            return open, closed
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
                children.append(board[x.location[0]][x.location[1]-1])

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
        # Lambda function to sort the open list
        open.sort(key=lambda q: q.f, reverse = True)


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


def heuristic(start, end): #Formula for Manhattan distance
    h = abs(start[0] - end[0]) + abs(start[1] - end[1])
    return h


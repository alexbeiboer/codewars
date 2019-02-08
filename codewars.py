import random
def make_make(size, lvl, st):
    # make a matrix with random ints
    matrix = [[random.randint(0,10) for row in range(size)] for col in range(size)]
    # loop through the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            # if element is > lvl = a free space
            if matrix[row][col] > lvl:
                matrix[row][col] = '.' # . = free space
                # else element is a wall
            else:
                matrix[row][col] = '|'
    x,y = st
    matrix[x][y] = "S"
    return matrix
def find_edges(matrix, node):
    x,y = node
    edges = []
    length = len(matrix)
    # add conditions for nw, sw, ne, se
    for x,y in (x, y+1), (x, y-1), (x+1, y), (x-1, y):
        if 0 <= x < length and 0 <= y < length:
            # check if matrix[x][y] is a free space
            if matrix[x][y] == '.':
                edges.append([x,y])
    return edges


maze = make_make(15,2, [0,0])


# init bfs
def bfs(maze, node):
    queue = [[node]]
    explored = []
    goal = [len(maze)-1, len(maze)-1]
    while queue:
        # FIFO
        path = queue.pop(0)
        node = path[-1]
        # check if we have searched path before
        if node not in explored:
            explored.append(node)
            # layer one connections to nod
            for edge in edges:
                new_list = list(path)
                queue.append(new_list)
                if edge == goal:
                    print(new_list)
                    for x,y in new_list:
                        maze[x][y] = 'X'
                    return maze
    return('no path found')
pprint.pprint(bfs(maze, (0,0)))

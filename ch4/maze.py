# Create the maze data structure:
# You can copy-paste this from inventwithpython.com/examplemaze.txt
MAZE = """
#######################################################################
#S#                 #       # #   #     #         #     #   #         #
# ##### ######### # ### ### # # # # ### # # ##### # ### # # ##### # ###
# #   #     #     #     #   # # #   # #   # #       # # # #     # #   #
# # # ##### # ########### ### # ##### ##### ######### # # ##### ### # #
#   #     # # #     #   #   #   #         #       #   #   #   #   # # #
######### # # # ##### # ### # ########### ####### # # ##### ##### ### #
#       # # # #     # #     # #   #   #   #     # # #   #         #   #
# # ##### # # ### # # ####### # # # # # # # ##### ### ### ######### # #
# # #   # # #   # # #     #     #   #   #   #   #   #     #         # #
### # # # # ### # # ##### ####### ########### # ### # ##### ##### ### #
#   # #   # #   # #     #   #     #       #   #     # #     #     #   #
# ### ####### ##### ### ### ####### ##### # ######### ### ### ##### ###
#   #         #     #     #       #   # #   # #     #   # #   # #   # #
### ########### # ####### ####### ### # ##### # # ##### # # ### # ### #
#   #   #       # #     #   #   #     #       # # #     # # #   # #   #
# ### # # ####### # ### ##### # ####### ### ### # # ####### # # # ### #
#     #         #     #       #           #     #           # #      E#
#######################################################################
""".split('\n')

MAZE = [list(x) for x in MAZE if x]

# Constants used in this program:
EMPTY = ' '
START = 'S'
EXIT = 'E'
PATH = '.'

def printMaze(maze):
    for y in range(HEIGHT):
        # Print each row.
        for x in range(WIDTH):
            # Print each column in this row.
            print(maze[y][x], end='')
        print()  # Print a newline at the end of the row.
    print()

# Get the height and width of the maze:
HEIGHT = len(MAZE)
WIDTH = len(MAZE[0])

def findStart(maze):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if maze[y][x] == START:
                return x, y  # Return the starting coordinates.

visited = set()

def mazeSolver(maze, x, y, visited):
    if (x, y) in visited or x < 0 or y < 0 or x >= WIDTH or y >= HEIGHT:
        return False
    if maze[y][x] == EXIT:
        return True
    if maze[y][x] not in (EMPTY, START):
        return False  # Only explore EMPTY and START cells

    visited.add((x, y))
    maze[y][x] = PATH

    print(visited)

    # go all directions
    s_r = mazeSolver(maze, x+1, y, visited)
    s_l = mazeSolver(maze, x-1, y, visited) 
    s_u = mazeSolver(maze, x, y-1, visited) 
    s_d = mazeSolver(maze, x, y+1, visited) 

    if s_r or s_l or s_u or s_d:
        return True

    maze[y][x] = EMPTY

    return False

def solveMaze(maze):
    tup = findStart(MAZE)
    if tup == None:
        return "No start found"
    x, y = tup
    solved = mazeSolver(maze, x, y, visited)
    print('Did we solve? ', solved)

printMaze(MAZE)
solveMaze(MAZE)
printMaze(MAZE)

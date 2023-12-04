import sys

im = [list('..########################...........'),
      list('..#......................#...#####...'),
      list('..#..........########....#####...#...'),
      list('..#..........#......#............#...'),
      list('..#..........########.........####...'),
      list('..######......................#......'),
      list('.......#..#####.....###########......'),
      list('.......####...#######................')]

HEIGHT = len(im)
WIDTH = len(im[0])

# implement flood fill
# visit all of the neighbors fropm each point
# base case is when you reach the end of the image, or when you reach a color
# is not the color that you are trying to change
# this has problems if there are a lot of characters to change all next to one another
# because then you would change a pixel, call another f, change and call
# and you would never return to that initial call
def floodFill(image, x, y, charToChangeTo, charToChange = None):
    if charToChange == None:
        charToChange = image[y][x]
    if charToChange != image[y][x] or charToChange == charToChangeTo:
        # you either reached a char which isn't the one to change OR
        # you already changed it
        return
    
    # you already handled the base cases, so...
    # change the character
    image[y][x] = charToChangeTo

    # visit all the neighbors from the starting point
    # move in x direction first
    if x + 1 < WIDTH and image[y][x + 1] == charToChange:
        floodFill(image, x + 1, y, charToChangeTo, charToChange)
    if x - 1 >= 0 and image[y][x - 1] == charToChange:
        floodFill(image, x - 1, y, charToChangeTo, charToChange)
    if y + 1 < HEIGHT and image[y + 1][x] == charToChange:
        floodFill(image, x, y + 1, charToChangeTo, charToChange)
    if y - 1 >= 0 and image[y - 1][x] == charToChange:
        floodFill(image, x, y - 1, charToChangeTo, charToChange)

    return

def printImage(image):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            sys.stdout.write(image[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')

# printImage(im)
# floodFill(im, 0, 0, "o", ".")
# printImage(im)

def printImageIter(image, x, y, newChar, oldChar = None):
    if oldChar == None:
        oldChar = image[y][x]

    stack = [(y, x)]

    while len(stack) > 0:
        y, x = stack.pop()

        currChar = image[y][x]

        if currChar != oldChar:
            continue

        image[y][x] = newChar

        if x + 1 < WIDTH and image[y][x + 1] == oldChar:
            stack.extend([(y, x + 1)])
        if x - 1 >= 0 and image[y][x - 1] == oldChar:
            stack.extend([(y, x - 1)])
        if y + 1 < HEIGHT and image[y + 1][x] == oldChar:
            stack.extend([(y + 1, x)])
        if y - 1 >= 0 and image[y - 1][x] == oldChar:
            stack.extend([(y - 1, x)])
    
    return

printImage(im)
printImageIter(im, 3, 3, 'x')
printImage(im)

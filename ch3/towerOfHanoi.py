import sys

TOTAL_DISKS = 3

TOWERS = {
        'A': list(reversed(range(1, TOTAL_DISKS + 1))),
        'B': [],
        'C': []
        }

def printDisk(diskNum):
    emptySpace = ' ' * (TOTAL_DISKS - diskNum)
    if diskNum == 0:
        sys.stdout.write(emptySpace + '||' + emptySpace)
    else:
        diskSpace = '@' * diskNum
        diskNumLabel = str(diskNum).rjust(2, '_')
        sys.stdout.write(emptySpace + diskSpace + diskNumLabel + diskSpace + emptySpace)

def printTowers():
    # Print all three towers.
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
            if level >= len(tower):
                printDisk(0)
            else:
                printDisk(tower[level])
        sys.stdout.write('\n')
    # Print the tower labels A, B, and C.
    emptySpace = ' ' * (TOTAL_DISKS)
    print('%s A%s%s B%s%s C\n' % (emptySpace, emptySpace, emptySpace, emptySpace, emptySpace))

def moveOneDisk(startTower, endTower):
    disk = TOWERS[startTower].pop()
    TOWERS[endTower].append(disk)

def solve(numberOfDisks, startTower, endTower, tempTower):
    # assume that this means one disk in the start category...
    if numberOfDisks == 1:
        moveOneDisk(startTower, endTower)
    else:
        solve(numberOfDisks - 1, startTower, tempTower, endTower)
        moveOneDisk(startTower, endTower)
        solve(numberOfDisks - 1, tempTower, endTower, startTower)

printTowers()
solve(TOTAL_DISKS, 'A', 'B', 'C')
printTowers()

# works with 2 as well bc you take the small one, move it to temp
# returns immediately afterwards
# then you move 2 to the end

# while True:
#    printTowers()
#    print('Enter letter of start tower and the end tower. (A, B, C) Or Q to quit.')
#    move = input().upper()
#    if move == 'Q':
#        sys.exit()
#    elif move[0] in 'ABC' and move[1] in 'ABC' and move[0] != move[1]:
#        moveOneDisk(move[0], move[1])

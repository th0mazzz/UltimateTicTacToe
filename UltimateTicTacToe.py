import os

# Variables to keep track of gameplay mechanics
board = dict() #Key is section id, value is list for that section
xTurn = True #Is it X's turn?
marks = {True: ' X', False: ' O'} #Used with xTurn to determine mark
gameEnded = False #Has game ended yet?
currentForce = None #Either none or a section id
taken = set() #Taken numbers (spots) go in
boardStatus = dict() #Keeps track of who won which section
winner = None #The winner's symbol when game ends (if tie, remains None)

def setupBoard():
# Sets up the initial game board numbers
    for i in range(9):
        boardStatus[i] = None
        if i == 0 or i == 1:
            digits = stringify(list(range(i*9, (i + 1)*9)))
            for d in range(len(digits)):
                if int(digits[d]) < 10:
                    digits[d] = '0' + digits[d]
            board[i] = digits
        else:
            board[i] = stringify(list(range(i*9, (i + 1)*9)))

def printBoard():
# Prints the current state of the large board
    smallRowsList = []
    for i in range(len(board)):

        smallRows = getSmallBoardRows(i)
        smallRowsList.append(smallRows)

    print(smallRowsList[0][0] + ' | ' + smallRowsList[1][0] + ' | ' + smallRowsList[2][0])
    print(smallRowsList[0][1] + ' | ' + smallRowsList[1][1] + ' | ' + smallRowsList[2][1])
    print(smallRowsList[0][2] + ' | ' + smallRowsList[1][2] + ' | ' + smallRowsList[2][2])
    print('---------------------------------')
    print(smallRowsList[3][0] + ' | ' + smallRowsList[4][0] + ' | ' + smallRowsList[5][0])
    print(smallRowsList[3][1] + ' | ' + smallRowsList[4][1] + ' | ' + smallRowsList[5][1])
    print(smallRowsList[3][2] + ' | ' + smallRowsList[4][2] + ' | ' + smallRowsList[5][2])
    print('---------------------------------')
    print(smallRowsList[6][0] + ' | ' + smallRowsList[7][0] + ' | ' + smallRowsList[8][0])
    print(smallRowsList[6][1] + ' | ' + smallRowsList[7][1] + ' | ' + smallRowsList[8][1])
    print(smallRowsList[6][2] + ' | ' + smallRowsList[7][2] + ' | ' + smallRowsList[8][2])

def getSmallBoardRows(section_id):
# Returns the small board's list rows as strings in a tuple based on section id
# For example: section 0 is
# 0 1 2
# 3 4 5
# 6 7 8
# would return ('00 01 02 ', '03 04 05 ', '06 07 08 ')
    smallBoardList = board[section_id]
    top = ""
    mid = ""
    bot = ""
    for i in range(len(smallBoardList)):
        if int(i) / 3 < 1:
            top = top + smallBoardList[i] + ' '
        elif int(i) / 3 < 2:
            mid = mid + smallBoardList[i] + ' '
        else:
            bot = bot + smallBoardList[i] + ' '
    return (top, mid, bot)

def stringify(list):
# Makes list of integers into list of stringed versions
    stringedList = []
    for element in list:
        stringedList.append(str(element))
    return stringedList

def markSpot(num, symbol):
# Marks spot number num with the symbol
    section_id = calcSection(num)
    smallBoardList = board[section_id]
    for i in range(len(smallBoardList)):
        if board[section_id][i].isnumeric() and int(board[section_id][i]) == int(selection):
            board[section_id][i] = symbol

def checkSmallBoardStatus(section_id):
# If a small board has a winner, update that in boardStatus and change all symbols in that section to winner's
    smallBoardList = board[section_id]
    for r in range(3):
        # Checks rows
        if smallBoardList[r*3] == smallBoardList[r*3 + 1] and smallBoardList[r*3] == smallBoardList[r*3 + 2] and boardStatus[section_id] == None:
            boardStatus[section_id] = smallBoardList[r*3]
            for i in range(len(smallBoardList)):
                if not(i == r*3 or i == r*3 + 1 or i == r*3 + 2):
                    smallBoardList[i] = '  '

        # Checks cols
        if smallBoardList[r] == smallBoardList[r + 3] and smallBoardList[r] == smallBoardList[r + 6] and boardStatus[section_id] == None:
            boardStatus[section_id] = smallBoardList[r]
            for i in range(len(smallBoardList)):
                if not(i == r or i == r + 3 or i == r + 6):
                    smallBoardList[i] = '  '

    # Checks diags
    if smallBoardList[0] == smallBoardList[4] and smallBoardList[0] == smallBoardList[8]:
        boardStatus[section_id] = smallBoardList[0]
        for i in range(len(smallBoardList)):
            if not(i == 0 or i == 4 or i == 8):
                smallBoardList[i] = '  '
    if smallBoardList[6] == smallBoardList[4] and smallBoardList[2] == smallBoardList[6]:
        boardStatus[section_id] = smallBoardList[2]
        for i in range(len(smallBoardList)):
            if not(i == 6 or i == 4 or i == 2):
                smallBoardList[i] = '  '

    # Checks for tie
    if smallBoardList.count(' X') + smallBoardList.count(' O') == 9:
        boardStatus[section_id] = ' -'
        for i in range(len(smallBoardList)):
            smallBoardList[i] = ' -'

def forceSection(num):
# Forces the user to select from a section based off number
# If section filled, free reign for user
# Returns the section id of the forced section
    force = num % 9
    if boardStatus[force] != None:
        return None
    return force

def calcSection(num):
# Given the spot number, return which section it is in
    return int(int(selection)/9)

def intify(list):
# Makes a list of strings into list of int, excludes the invalid items
    intified = []
    for i in range(len(list)):
        if list[i].isnumeric():
            intified.append(int(list[i]))
    return intified

def checkBoardStatus():
# If game has ended, set gameEnded to True
# If there is a winner, set variable winner to winner's symbol (if tie, symbol is ' -')

    global gameEnded
    global winner

    for r in range(3):
        # Checks rows
        if boardStatus[r*3] == boardStatus[r*3 + 1] and boardStatus[r*3] == boardStatus[r*3 + 2] and boardStatus[r*3] != ' -' and boardStatus[r*3] != None:
            gameEnded = True
            winner = boardStatus[r*3]

        # Checks cols
        if boardStatus[r] == boardStatus[r + 3] and boardStatus[r] == boardStatus[r + 6] and boardStatus[r] != ' -' and boardStatus[r] != None:
            gameEnded = True
            winner = boardStatus[r]

    # Checks diags
    if boardStatus[4] != ' -' and boardStatus[4] != None:
        if boardStatus[0] == boardStatus[4] and boardStatus[0] == boardStatus[8]:
            gameEnded = True
            winner = boardStatus[0]
        if boardStatus[2] == boardStatus[4] and boardStatus[2] == boardStatus[6]:
            gameEnded = True
            winner = boardStatus[2]

    # Checks for tie
    tie = True
    for section in boardStatus:
        if boardStatus[section] == None:
            tie = False
    if tie:
        gameEnded = True



setupBoard()
os.system('clear')
while not gameEnded:
    printBoard()
    print('\nIt is ' + marks[xTurn] + "'s turn.")

    # Checks to make sure input is valid
    if currentForce == None:
        selection = input('Please enter any non-taken number: ')
        while not selection.isnumeric() or selection in taken or int(selection) > 80 or int(selection) < 0:
            selection = input('Invalid input. Please enter any non-taken number: ')
    else:
        forcedNums = intify(board[currentForce])
        selection = input('Please enter a non-taken number in ' + str(forcedNums) + ' :')
        while not selection.isnumeric() or selection in taken or int(selection) not in forcedNums or int(selection) > 80 or int(selection) < 0:
            selection = input('Invalid input. Please enter a non-taken number in the list: ')

    taken.add(selection)
    markSpot(selection, marks[xTurn])
    section_id = calcSection(selection)
    checkSmallBoardStatus(section_id)
    checkBoardStatus()
    currentForce = forceSection(int(selection))
    xTurn = not xTurn
    os.system('clear')

if winner == None:
    print('The game was a tie.')
    printBoard()
else:
    printBoard()
    print('The winner was' + winner + '!')

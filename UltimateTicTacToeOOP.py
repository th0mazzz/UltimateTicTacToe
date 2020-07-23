class SmallBoard:
    def __init__(self, id):
        self.spots = []
        for i in range(9*id, 9*id + 9):
            if i > 9:
                self.spots.append(str(i))
            else:
                self.spots.append('0' + str(i))
        print(self.spots)

    def printboard(self):
    # Used for debugging
        print(self.spots[0:3])
        print(self.spots[3:6])
        print(self.spots[6:9])

    def markSpot(self, spotNum, marker):
        index = int(spotNum) % 9
        self.spots[index] = marker

    def checkSmallBoardStatus(self):
    # If a small board has a winner, update that in boardStatus and change all symbols in that section to winner's
        smallBoardList = self.spots
        boardStatus = board.boardStatus
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

class LargeBoard:

    def __init__(self):
        self.smallboards = dict()
        self.taken = set()
        self.boardStatus = dict()
        self.winner = None
        self.gameEnded = False
        self.xTurn = True
        self.markers = {True: ' X', False: ' O'}
        self.force = None

        for i in range(9):
            self.smallboards[i] = SmallBoard(i)
            self.boardStatus[i] = None

    def printboard(self):
        smallboards = self.smallboards
        for times in range(3):
            if times != 0:
                print('---------------------------------')
            for i in range(3):
                string = ''
                for j in range(times*3, times*3 + 3):
                    for k in range(i*3, i*3 + 3):
                        string = string + smallboards[j].spots[k] + ' '
                    string = string + ' | '
                string = string[:len(string) - 3]
                print(string)

    def markSpot(self, spotNum, marker):
        smallboardNum = int(spotNum) // 9
        self.smallboards[smallboardNum].markSpot(spotNum, marker)

    def checkBoardStatus(self):
    # If game has ended, set gameEnded to True
    # If there is a winner, set variable winner to winner's symbol (if tie, symbol is ' -')

        boardStatus = self.boardStatus

        for r in range(3):
            # Checks rows
            if boardStatus[r*3] == boardStatus[r*3 + 1] and boardStatus[r*3] == boardStatus[r*3 + 2] and boardStatus[r*3] != ' -' and boardStatus[r*3] != None:
                self.gameEnded = True
                self.winner = boardStatus[r*3]

            # Checks cols
            if boardStatus[r] == boardStatus[r + 3] and boardStatus[r] == boardStatus[r + 6] and boardStatus[r] != ' -' and boardStatus[r] != None:
                self.gameEnded = True
                self.winner = boardStatus[r]

        # Checks diags
        if boardStatus[4] != ' -' and boardStatus[4] != None:
            if boardStatus[0] == boardStatus[4] and boardStatus[0] == boardStatus[8]:
                self.gameEnded = True
                self.winner = boardStatus[0]
            if boardStatus[2] == boardStatus[4] and boardStatus[2] == boardStatus[6]:
                self.gameEnded = True
                self.winner = boardStatus[2]

        # Checks for tie
        tie = True
        for section in boardStatus:
            if boardStatus[section] == None:
                tie = False
        if tie:
            self.gameEnded = True

    def checkSmallBoardStatus(self, id):
        self.smallboards[id].checkSmallBoardStatus()

    def forceSection(self, num):
    # Forces the user to select from a section based off number
    # If section filled, free reign for user
    # Returns the section id of the forced section
        force = num % 9
        if self.boardStatus[force] != None:
            return None
        return force

    def calcSection(self, num):
    # Given the spot number, return which section it is in
        return int(int(selection)/9)

    def intify(self, smallboard):
    # Makes a list of strings into list of int, excludes the invalid items
        intified = []
        for i in range(len(smallboard.spots)):
            if smallboard.spots[i].isnumeric():
                intified.append(int(smallboard.spots[i]))
        return intified


import os

board = LargeBoard()
os.system('clear')
while not board.gameEnded:
    board.printboard()
    print(board.boardStatus)
    print('\nIt is ' + board.markers[board.xTurn] + "'s turn.")

    # Checks to make sure input is valid
    if board.force == None:
        selection = input('Please enter any non-taken number: ')
        while not selection.isnumeric() or selection in board.taken or int(selection) > 80 or int(selection) < 0:
            selection = input('Invalid input. Please enter any non-taken number: ')
    else:
        forcedNums = board.intify(board.smallboards[board.force])
        selection = input('Please enter a non-taken number in ' + str(forcedNums) + ' :')
        while not selection.isnumeric() or selection in board.taken or int(selection) not in forcedNums or int(selection) > 80 or int(selection) < 0:
            selection = input('Invalid input. Please enter a non-taken number in the list: ')

    board.taken.add(selection)
    board.markSpot(selection, board.markers[board.xTurn])
    section_id = board.calcSection(selection)
    board.checkSmallBoardStatus(section_id)
    board.checkBoardStatus()
    board.force = board.forceSection(int(selection))
    board.xTurn = not board.xTurn
    os.system('clear')

if board.winner == None:
    print('The game was a tie.')
    board.printboard()
else:
    board.printboard()
    print('The winner was' + board.winner + '!')

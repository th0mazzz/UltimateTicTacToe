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


class LargeBoard:
    smallboards = []
    def __init__(self):
        for i in range(9):
            self.smallboards.append(SmallBoard(i))

    def printboard(self):

        smallRowsList = self.smallboards

        for i in range(9):
            string = ''
            for j in range(3):
                string = string +

            print(smallRowsList[i].spots[0] + ' ' + smallRowsList[i].spots[1] + ' ' + smallRowsList[i].spots[2] + ' | ')
            print(smallRowsList[0].spots[1] + ' | ' + smallRowsList[1].spots[1] + ' | ' + smallRowsList[2].spots[1])
            print(smallRowsList[0].spots[2] + ' | ' + smallRowsList[1].spots[2] + ' | ' + smallRowsList[2].spots[2])
            print('---------------------------------')
        # print(smallRowsList[3][0] + ' | ' + smallRowsList[4][0] + ' | ' + smallRowsList[5][0])
        # print(smallRowsList[3][1] + ' | ' + smallRowsList[4][1] + ' | ' + smallRowsList[5][1])
        # print(smallRowsList[3][2] + ' | ' + smallRowsList[4][2] + ' | ' + smallRowsList[5][2])
        # print('---------------------------------')
        # print(smallRowsList[6][0] + ' | ' + smallRowsList[7][0] + ' | ' + smallRowsList[8][0])
        # print(smallRowsList[6][1] + ' | ' + smallRowsList[7][1] + ' | ' + smallRowsList[8][1])
        # print(smallRowsList[6][2] + ' | ' + smallRowsList[7][2] + ' | ' + smallRowsList[8][2])

board = LargeBoard()
board.printboard()

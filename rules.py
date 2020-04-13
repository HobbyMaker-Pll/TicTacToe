import numpy as np


class Rule(object):
    def __init__(self, grid, drawPerTurn):
        # Creating internal data for check
        self.grid = grid
        self.turn = np.random.choice(('X', 'O'))
        self.turns_taken = 0
        self.gameData = []
        self.resetGameData()

        self.DrawPerTurn = drawPerTurn
        self.Draw_taken = 0

    def resetGameData(self):
        self.gameData = [[None for _ in range(self.grid)] for _ in range(self.grid)]
        self.turns_taken = 0
        self.Draw_taken = 0

    def setGameData(self, x, y):
        self.gameData[x - 1][y - 1] = self.turn
        self.turns_taken += 1

    def is_Available(self, x, y):
        if self.gameData[x - 1][y - 1] is None:
            return True
        else:
            return False

    def checkDrawsperturn(self):
        self.Draw_taken += 1
        if self.Draw_taken == self.DrawPerTurn:
            self.Draw_taken = 0
            return True
        else:
            return False

    def invertTurn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def getTurn(self):
        return self.turn

    def is_Won(self, x, y):
        if self.checkCol(x) or self.checkRow(y) or self.checkBackSlash() or self.checkSlash():
            return True
        else:
            return False

    def is_Draw(self):
        if self.turns_taken == np.power(self.grid, 2):
            return True
        else:
            return False

    def checkWin(self, quantity):
        if quantity == self.grid:
            return True
        else:
            return False

    def checkCol(self, x):
        # Checks how many times the sign appears in the Col
        counter = 0

        for col in self.gameData[x - 1]:
            if col == self.turn:
                counter += 1

        return self.checkWin(counter)

    def checkRow(self, y):
        # Checks how many times the sign appears in the Row
        tGamedata = np.transpose(self.gameData)
        counter = 0

        for row in tGamedata[y - 1]:
            if row == self.turn:
                counter += 1

        return self.checkWin(counter)

    def checkSlash(self):
        counter = 0
        for cel in range(self.grid):
            if self.gameData[cel][cel] == self.turn:
                counter += 1

        return self.checkWin(counter)

    def checkBackSlash(self):
        rGrid = list(reversed(range(0, self.grid)))
        counter = 0

        for cel in range(self.grid):
            if self.gameData[rGrid[cel]][cel] == self.turn:
                counter += 1

        return self.checkWin(counter)

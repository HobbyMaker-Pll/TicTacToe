import tkinter as tk
from math import *
from tkinter import messagebox
from gameInterface import Interface
from scoreBoard import Scores
from rules import Rule


def ratio(value, proportion):
    return floor(value / proportion)


class Game(object):

    def __init__(self, root, configs):

        # Loading configurations to self variables
        self.tableSize = configs["tableSize"]
        self.grid = configs["grid"]
        self.drawPerTurn = configs["drawPerTurn"]
        self.btwLines = (self.tableSize / self.grid)

        self.fontSize = self.gridOffset = ratio(self.tableSize, 30)
        self.lineWidth = ratio(self.tableSize, 100)

        # Creating major pieces for the game interface
        self.rule = Rule(self.grid, self.drawPerTurn)
        self.root = root
        self.canvas = tk.Canvas(root,
                                width=self.tableSize,
                                height=self.tableSize,
                                bg="black", highlightthickness=0)

        self.Fscoreboard = tk.Frame(root, bg="black")

        self.canvas.pack(expand=False, side=tk.LEFT, padx=10, pady=10)
        self.Fscoreboard.pack(fill=tk.X, expand=True, side=tk.RIGHT, padx=10)

        # Creating minor pieces for the game interface
        font_Type = f"Verdana {self.fontSize} bold"

        self.scoreTitle = tk.Label(self.Fscoreboard, text="ScoreBoard", font=font_Type,
                                   fg="White", bg="black")

        self.scoreStatus = tk.Label(self.Fscoreboard, text="0 ⇦ O | X ⇨ 0", font=font_Type,
                                    fg="White", bg="black")
        self.Draws = tk.Label(self.Fscoreboard, text="Draws: 0", font=font_Type,
                              fg="White", bg="black")

        self.Rounds = tk.Label(self.Fscoreboard, text="Round: 0", font=font_Type,
                               fg="White", bg="black")

        self.Turn = tk.Label(self.Fscoreboard, text=f"{self.rule.getTurn()} ⇦ Turn", font=font_Type,
                             fg="White", bg="black")

        self.bReset = tk.Button(self.Fscoreboard, text="Reset", font=font_Type,
                                fg="White", bg="black",
                                activeforeground="White", activebackground="Black",
                                borderwidth=0, relief="flat",
                                command=self.reset_onClick)
        self.scoreTitle.pack()
        self.scoreStatus.pack(side=tk.TOP)
        self.Draws.pack(side=tk.TOP)
        self.Turn.pack(side=tk.TOP, pady=20)
        self.Rounds.pack(side=tk.TOP)
        self.bReset.pack(side=tk.TOP)
        # Binding methods to the events
        self.canvas.bind("<Button-1>", self.canvas_onClick)

        # Loading instances into self variables
        self.scoreboard = Scores(self.scoreStatus, self.Rounds, self.Draws, self.Turn)
        self.g_interface = Interface(self.canvas, self.tableSize, self.grid,
                                     self.lineWidth, self.gridOffset)

        # Reset lines
        self.g_interface.resetBoard()

    def canvas_onClick(self, event):
        """
        Draws the X or O if possible, asks the game data if someone has won
        :param event:
        :return: nothing
        """
        # Getting posX and posY as divisions based on table cord
        x = ceil(event.x / self.btwLines)
        y = ceil(event.y / self.btwLines)

        # Asks if the space is available
        if self.rule.is_Available(x, y):

            if self.rule.getTurn() == 'X':
                self.g_interface.draw_X(x, y)
            else:
                self.g_interface.draw_O(x, y)

            # Set the draw piece into the game data
            self.rule.setGameData(x, y)

            # Analise the game....
            # check if rol or coll or cross have 3 signs equal
            if self.rule.is_Won(x, y):
                messagebox.showinfo("Winner",
                                    f"{self.rule.getTurn()} has won the Match")
                self.scoreboard.incScore(self.rule.getTurn())
                self.g_interface.resetBoard()
                self.rule.resetGameData()
                self.rule.invertTurn()
                self.scoreboard.changeTurn(self.rule.getTurn())

            # checks if the game has not draw of turns
            elif self.rule.is_Draw():
                messagebox.showinfo("Draw",
                                    "This match ended in a Draw :(")
                self.scoreboard.incDraw()
                self.g_interface.resetBoard()
                self.rule.resetGameData()
                self.rule.invertTurn()
                self.scoreboard.changeTurn(self.rule.getTurn())

            else:
                if self.rule.checkDrawsperturn():
                    self.rule.invertTurn()
                    self.scoreboard.changeTurn(self.rule.getTurn())

    def reset_onClick(self):
        self.scoreboard.resetScores()
        self.g_interface.resetBoard()
        self.rule.resetGameData()
        messagebox.showinfo("Restarted",
                            "The game was restarted good luck :)")

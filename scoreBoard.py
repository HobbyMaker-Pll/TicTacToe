import tkinter as tk


class Scores(object):

    def __init__(self, label_Score, label_Rounds, label_Draws, label_Turn):
        self.Score = {
            'X': 0,
            'O': 0
        }
        self.Round = 0
        self.Draws = 0
        self.label_Score = label_Score
        self.label_Rounds = label_Rounds
        self.label_Draws = label_Draws
        self.label_Turn = label_Turn

    def changeTurn(self, who):
        self.label_Turn.config(text=f"{who} ⇦ Turn")

    def incScore(self, who):
        self.Score[who] += 1
        self.setNewScore(self.Score['O'], self.Score['X'])
        self.incRound()

    def incDraw(self):
        self.Draws += 1
        self.label_Draws.config(text=f"Draws: {self.Draws}")
        self.incRound()

    def incRound(self):
        self.Round += 1
        self.label_Rounds.config(text=f"Round: {self.Round}")

    def resetScores(self):
        self.Score['X'] = 0
        self.Score['O'] = 0
        self.Draws = 0
        self.Round = 0
        self.setNewScore(self.Score['O'], self.Score['X'])
        self.label_Rounds.config(text=f"Round: {self.Round}")
        self.label_Draws.config(text=f"Draws: {self.Draws}")

    def setNewScore(self, O, X):
        self.label_Score.config(text=f"{O} ⇦ O | X ⇨ {X}")

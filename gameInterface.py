import tkinter as tk
from tkinter import messagebox
from math import *


class Interface(object):

    def __init__(self, canvas, tableSize, grid, lineWidth, gridOffset):

        # loading configurations from json file into self variables
        self.canvas = canvas
        self.tableSize = tableSize
        self.grid = grid
        self.lineWidth = lineWidth
        self.gridOffset = gridOffset
        self.btwLines = (self.tableSize / self.grid)

    def getDrawCords(self, x, y):
        """
        Calculates the cords to draw with the configured offset
        :param x: x pos
        :param y: y pos
        :return: Tuple with max and min values to draw
        """
        # Getting absolute coords
        x_Ref = x * self.btwLines
        y_Ref = y * self.btwLines

        # Calculating offset and positions
        x_Max = x_Ref - self.gridOffset
        x_Min = (x_Ref - self.btwLines) + self.gridOffset
        y_Max = y_Ref - self.gridOffset
        y_Min = (y_Ref - self.btwLines) + self.gridOffset

        return x_Max, y_Max, x_Min, y_Min

    def draw_O(self, x, y):
        """
        Draws a O based on the clicked position
        :param x: x pos
        :param y: y pos
        :return: None
        """
        results = self.getDrawCords(x, y)

        self.canvas.create_oval(results[2], results[3],
                                results[0], results[1],
                                width=self.lineWidth, outline="white")

    def draw_X(self, x, y):
        """
        Draws a X based on the clicked position
        :param x: x pos
        :param y: y pos
        :return: None
        """
        results = self.getDrawCords(x, y)

        self.canvas.create_line(results[2], results[3],
                                results[0], results[1],
                                width=self.lineWidth, fill="white")

        self.canvas.create_line(results[0], results[3],
                                results[2], results[1],
                                width=self.lineWidth, fill="white")

    def resetBoard(self):
        """
        Draws the table lines based on the configured table size, lines width and grid layout
        :return: none
        """
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, self.tableSize, self.tableSize, width=self.lineWidth, outline="white")
        for i in range(1, self.grid):
            pos = self.btwLines * i
            self.canvas.create_line(pos, 0, pos, self.tableSize, width=self.lineWidth, fill="white")
            self.canvas.create_line(0, pos, self.tableSize, pos, width=self.lineWidth, fill="white")

from time import sleep
from graphics import *
from board import *
from nuclear_missile import *


class small_missile(nuclear_missile):
    """docstring for small_missile."""

    def __init__(self, g, x, y, val, glob):
        self.x = x
        self.y = y
        self.draw(g, "l")
        self.val = val
        self.t = glob
        self.flg = 0
        self.mark = 0.5


if __name__ == '__main__':
    g = GraphWin("game ", 4000, 1500)
    score = board(g)
    s = 'p'
    mis = small_missile(g, 200, 900)
    mis.launch(g, [], 0.5)

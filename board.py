from graphics import *
from os import system


class board(object):
    """docstring for board."""

    def score_draw(self, g):
        msg = Text(Point(1100, 100), "SCORE :")
        msg.setSize(24)
        msg.setFill("red")
        msg.draw(g)

    def score_update(self, g, a):
        self.score.setText(a)

    def __init__(self, g):
        sqr = Rectangle(Point(100, 100), Point(1000, 1000))
        sqr.draw(g)
        sqr.setOutline("blue")
        self.score_draw(g)
        #self.score_update(g, 0)
        self.score = Text(Point(1200, 100), 0)
        self.score.setSize(24)
        self.score.setFill("red")
        self.score.draw(g)


if __name__ == '__main__':
    g = GraphWin("game ", 4000, 1500)
    score = board(g)
    s = 'p'
    while s != 'q':
        s = raw_input("Enter Q to exit : ")
        os.system("clear")

from time import sleep
from graphics import *
from board import *
from alien import *
from space_ship import *


class nuclear_missile(object):
    """docstring for nuclear_missile."""

    def draw(self, g, k):
        self.mis = Text(Point(self.x, self.y), k)
        self.mis.setSize(18)
        self.mis.draw(g)
        self.mis.setFill("red")

    def __init__(self, g, x, y, val, glob):
        self.x = x
        self.y = y
        self.draw(g, "i")
        self.val = val
        self.t = glob
        self.flg = 0
        self.mark = 1

    def launch(self, g, aln, feil, glob):
        #print("%d %d") % (glob - self.t, self.y)
        if self.y >= 100 and glob - self.t >= self.mark:
            # print("yes")
            self.t = glob
            pt = Point(self.x, self.y)
            chk = alien.check(aln.a, g, aln, feil, self.val, glob, pt)
            self.mis.move(0, -100)
            self.y -= 100
            if chk == 1:
                self.flg = 1
                self.mis.undraw()
                return (800 - self.y) / 100
            if self.y == 100:
                self.flg = 1
            # time.sleep(val)
        elif self.flg == 1:
            self.mis.undraw()
            return (800 - self.y) / 100


if __name__ == '__main__':
    g = GraphWin("game ", 4000, 1500)
    score = board(g)
    s = 'p'
    mis = nuclear_missile(g, 300, 900)
    while True:
        g.update()
        g.update_idletasks()

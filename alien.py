from time import sleep
from graphics import *
from board import *
import random


class alien(object):
    """docstring for alien."""

    def draw(self, g):
        self.aln = Text(Point(self.x, self.y), "@")
        self.aln.setSize(24)
        self.aln.draw(g)
        self.aln.setFill("red")

    def __init__(self, g, x, y, glob):
        self.x = x * 100
        self.y = y * 100
        self.t = glob
        self.s = glob
        self.val = 1
        self.draw(g)

    @staticmethod
    def update(a):
        for i in a:
            i.t += 1

    @staticmethod
    def check(a, g,  aln, feil, val, glob, pt=Point(0, 0)):
        for i in a:
            if i.t - i.s > 8:
                i.aln.undraw()
                a.remove(i)
            elif i.x == pt.x and i.y == pt.y:
                i.val -= val
                if i.val <= 0:
                    i.aln.undraw()
                    a.remove(i)
                    aln.score += 1
                    feil.score_update(g, aln.score)
                    return 1
                if val == 0.5:
                    i.aln.setText('a')
                    i.t += 3
                else:
                    i.aln.undraw()
                    a.remove(i)
        return 0


if __name__ == '__main__':
    g = GraphWin("game ", 4000, 1500)
    score = board(g)
    s = 'p'
    cnt = 0
    a = []
    while s != 'Q':
        if cnt % 10 == 0:
            tmp = alien(g, random.randint(3, 9), random.randint(2, 9))
            a.append(tmp)
        cnt += 1
        alien.update(a)
        alien.check(a, g)
        time.sleep(1)

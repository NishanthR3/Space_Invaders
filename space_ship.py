from graphics import *
from board import *
from nuclear_missile import *
from small_missile import *
from time import sleep


class space_ship(object):
    """docstring for space_ship."""

    def draw(self, g):
        self.ship = Text(Point(200, 900), "#")
        self.ship.setSize(24)
        self.ship.setFill("green")
        self.ship.draw(g)

    def __init__(self, g):
        self.draw(g)
        self.x = 200
        self.y = 900

    def mov(self, key, g, aln, feil, glob):
        if key == 'A' and self.x >= 300:
            self.x -= 100
            self.ship.move(-100, 0)

        elif key == 'D' and self.x <= 800:
            self.x += 100
            self.ship.move(100, 0)

        elif key == ' ':
            mis = nuclear_missile(g, self.x, self.y, glob, 1)
            mis.launch(g, aln, feil, glob)
            del mis

        elif key == 'S':
            mis = small_missile(g, self.x, self.y, glob, 0.5)
            mis.launch(g, aln, feil, glob)
            del mis

        elif key == 'Q':
            aln.flag = 1


if __name__ == '__main__':
    g = GraphWin("game ", 4000, 1500)
    score = board(g)
    s = 'p'
    ship = space_ship(g)
    while s != 'Q':
        s = raw_input("Enter Q to exit : ")
        ship.mov(s, g)
        os.system("clear")

from graphics import *
from board import *
from time import *
from space_ship import *
from nuclear_missile import *
from small_missile import *
from alien import *
if __name__ == '__main__':

    class graphic1(GraphWin):
        def _onKey(self, evnt):
            self.lastKey = evnt.keysym
            if evnt.char == 'A' or evnt.char == 'D' or evnt.char == 'Q':
                ship.mov(evnt.char, g, aln, feil, cnter)
            elif evnt.char == ' ':
                tmp = nuclear_missile(g, ship.x, ship.y - 100, 1, time.time())
                mis.append(tmp)
            elif evnt.char == 'S':
                tmp = small_missile(g, ship.x, ship.y - 100, 0.5, time.time())
                mis.append(tmp)

    g = graphic1("game ", 4000, 1500)
    s = 'p'

    class aln:
        pass
    aln.a = []
    aln.cnt = 0
    aln.score = 0
    aln.flag = 0

    mis = []

    feil = board(g)
    ship = space_ship(g)

    start = time.time()
    cnter = time.time()
    c = time.time()

    tmp = alien(g, random.randint(2, 9), random.randint(2, 3), start)
    aln.a.append(tmp)

    while True:
        alien.check(aln.a, g, aln, feil, 1, time.time())
        for i in mis:
            i.launch(g, aln, feil, time.time())
        if time.time() - cnter >= 1:
            alien.update(aln.a)
            cnter = time.time()
        if time.time() - start >= 10:
            start = time.time()
            tmp = alien(g, random.randint(3, 9), random.randint(2, 3), start)
            aln.a.append(tmp)
        if aln.flag == 1:
            break
        g.update()
        g.update_idletasks()
    g.close()

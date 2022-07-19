import pygame as pg
import Engine
from os import system

WIDTH = HEIGHT = 600
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('MK Chess')
FPS = 60
bdsz = 600
sqsz = bdsz/8
pcnm = ['wp1', 'wp2', 'wp3', 'wp4', 'wR1', 'wR2', 'wN1', 'wN2',
        'bp1', 'bp2', 'bp3', 'bp4', 'bR1', 'bR2', 'bN1', 'bN2',
        'bB1', 'bB2', 'wB1', 'wB2', 'wp6', 'wp7', 'wp8', 'bp5',
        'bp6', 'bp7', 'bp8', 'wp5', 'wK' , 'wQ' , 'bK' , 'bQ' ]

pcload = [{'id': p,
           'img': pg.transform.scale(pg.image.load('pcs/' + p[:2] + '.png'), (sqsz, sqsz)),
           'pos': (0, 0),
           'type': p[:2]} for p in pcnm]

board = Engine.Board(pcload, sqsz)
board.resetboard()
sqsl = [(-1, -1), (-1, -1)]


def draw(click, mpos):
    drawboard()
    draweffects(click, mpos)
    drawpieces()
    drawmoving(mpos)
    pg.display.update()


def drawboard():
    cor = [pg.Color(255, 255, 255), pg.Color(255, 150, 150)]
    for x in range(8):
        for x1 in range(8):
            sqcor = cor[(x + x1) % 2]
            pg.draw.rect(WIN, sqcor, pg.Rect(x*sqsz, x1*sqsz, sqsz, sqsz))


def draweffects(click, mpos):
    if click:
        mx, my = mpos
        mx = mx // sqsz
        my = my // sqsz
        pg.draw.rect(WIN, (255, 100, 100), pg.Rect(mx*sqsz, my*sqsz, sqsz, sqsz))


def drawmoving(mpos):
    for pc in board.board:
        if board.moving is not None:
            if board.moving['id'] == pc['id']:
                mx, my = mpos
                mx -= sqsz / 2
                my -= sqsz / 2
                pc['pos'] = (-1, -1)
                WIN.blit(board.moving['img'], (mx, my))


def drawpieces():
    for pc in board.board:
        if pc['pos'] != (-1, -1):
            WIN.blit(pc['img'], pc['pos'])


def main():
    run = True
    clock = pg.time.Clock()
    click = False

    while run:

        clock.tick(FPS)
        mpos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_0:
                    board.resetboard()

            if event.type == pg.MOUSEBUTTONDOWN:
                a1, a2 = mpos[0] // sqsz, mpos[1] // sqsz
                a1, a2 = a1 * sqsz, a2 * sqsz
                click = True
                for e in board.board:
                    if e['pos'] == (a1, a2):
                        board.moving = e.copy()

            elif event.type == pg.MOUSEBUTTONUP:
                a1, a2 = mpos[0] // sqsz, mpos[1] // sqsz
                a1, a2 = a1 * sqsz, a2 * sqsz
                board.moving2 = (a1, a2)

                if click:
                    if board.moving['id'] != 'null':
                        val = board.validate(board.moving, board.moving2)
                        if val:
                            board.moving['pos'] = board.moving2
                            a = board.moving
                            board.stopmoving(a, board.moving2)
                        else:
                            board.failmove()
                    click = False

        draw(click, mpos)

    pg.quit()

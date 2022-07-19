
class Board:
    def __init__(self, x, sqsz):
        self.board = x
        self.moving = {'id': 'null'}
        self.moving2 = ()
        self.sqsz = sqsz

    def validate(self, x, y):
        pcnm = x['id']
        a = x['pos']
        a1, a2 = a[0] // self.sqsz, a[1] // self.sqsz
        b1, b2 = y[0] // self.sqsz, y[1] // self.sqsz
        a = (a1, a2)
        b = (b1, b2)
        vld = False
        if pcnm[1] == 'p':
            vld = self.pawn(pcnm, a, b)
        elif pcnm[1] == 'R':
            vld = self.rook(a, b)
        elif pcnm[1] == 'N':
            vld = self.knight(a, b)
        elif pcnm[1] == 'B':
            vld = self.bishop(a, b)
        elif pcnm[1] == 'Q':
            vld = self.queen(a, b)
        elif pcnm[1] == 'K':
            vld = self.king(a, b)

        if vld:
            for x32 in self.board:
                if x32['pos'] == y:
                    a32 = x32['id']
                    a33 = x['id']
                    if a32[0] == a33[0]:
                        vld = False


        if vld:
            print(f'{pcnm} movido de {a1, a2} para {b1, b2}')
            return True

        else:
            return False

    def failmove(self):
        for x in self.board:
            if self.moving['id'] == x['id']:
                x['pos'] = self.moving['pos']
                self.moving = {'id': 'null'}

    def pawn(self, pcnm, a, b):
        a1, a2 = a[0], a[1]
        b1, b2 = b[0], b[1]
        c1 , c2 = b1 * self.sqsz, b2 * self.sqsz
        atk = False
        for x32 in self.board:
            if x32['pos'] == (c1, c2):
                a32 = x32['id']
                if pcnm[0] != a32[0]:
                    atk = True

        valid = False

        if pcnm[0] == 'w':
            if ((not atk) and (a1 == b1) and (a2 == b2 + 1)) \
            or ((not atk) and ((a1 == b1) and (a2 == b2 + 2)) and a2 == 6)\
            or (atk and ((a1 - b1 in (1, -1)) and (a2 == b2 + 1))):
                valid = True

        if pcnm[0] == 'b':
            if ((not atk) and (a1 == b1) and (a2 == b2 - 1)) \
            or ((not atk) and ((a1 == b1) and (a2 == b2 - 2)) and a2 == 1)\
            or (atk and ((a1 - b1 in (1, -1)) and (a2 == b2 - 1))):
                valid = True
        return valid

    def rook(self, a, b):
        a1, a2 = a[0], a[1]
        b1, b2 = b[0], b[1]
        valid = False
        if ((a1 == b1) and (a2 != b2)) or ((a1 != b1) and (a2 == b2)):
            valid = True
        return valid

    def knight(self, a, b):
        a1, a2 = a[0], a[1]
        b1, b2 = b[0], b[1]
        valid = False
        if (((a1 == (b1 + 2)) or (a1 == (b1 - 2))) and ((a2 == (b2 + 1)) or (a2 == (b2 - 1)))) \
        or (((a2 == (b2 + 2)) or (a2 == (b2 - 2))) and ((a1 == (b1 + 1)) or (a1 == (b1 - 1)))):
            valid = True
        return valid

    def bishop(self, a, b):
        a1, a2 = a[0], a[1]
        b1, b2 = b[0], b[1]
        valid = False
        if ((a1 - b1) == (a2 - b2)) or ((a1 - b1) == ((a2 - b2) * -1)) \
        and ((a2 != b2) or (a1 != b1)):
            valid = True
        return valid

    def queen(self, a, b):
        a1, a2 = a[0], a[1]
        b1, b2 = b[0], b[1]
        valid = False
        if (((a1 - b1) == (a2 - b2)) or ((a1 - b1) == ((a2 - b2) * -1))
        and ((a2 != b2) or (a1 != b1))) \
        or ((a1 == b1) and (a2 != b2)) or ((a1 != b1) and (a2 == b2)):
            valid = True
        return valid

    def king(self, a, b):
        a1, a2 = a[0], a[1]
        b1, b2 = b[0], b[1]
        valid = False
        if b1 - a1 in (0, 1, -1) and b2 - a2 in (0, 1, -1):
            valid = True
        return valid

    def resetboard(self):
        resetpos = [{'id':'wp1', 'pos': (0, 6)}, {'id':'wp2', 'pos': (1, 6)}, {'id':'wp3', 'pos': (2, 6)},
                    {'id':'wp4', 'pos': (3, 6)}, {'id':'wp5', 'pos': (4, 6)}, {'id':'wp6', 'pos': (5, 6)},
                    {'id':'wp7', 'pos': (6, 6)}, {'id':'wp8', 'pos': (7, 6)}, {'id':'bp1', 'pos': (0, 1)},
                    {'id':'bp2', 'pos': (1, 1)}, {'id':'bp3', 'pos': (2, 1)}, {'id':'bp4', 'pos': (3, 1)},
                    {'id':'bp5', 'pos': (4, 1)}, {'id':'bp6', 'pos': (5, 1)}, {'id':'bp7', 'pos': (6, 1)},
                    {'id':'bp8', 'pos': (7, 1)}, {'id':'wR1', 'pos': (0, 7)}, {'id':'wN1', 'pos': (1, 7)},
                    {'id':'wB1', 'pos': (2, 7)}, {'id':'wB2', 'pos': (5, 7)}, {'id':'wN2', 'pos': (6, 7)},
                    {'id':'wR2', 'pos': (7, 7)}, {'id':'bN2', 'pos': (6, 0)}, {'id':'bR2', 'pos': (7, 0)},
                    {'id':'bR1', 'pos': (0, 0)}, {'id':'bN1', 'pos': (1, 0)}, {'id':'bB1', 'pos': (2, 0)},
                    {'id':'bB2', 'pos': (5, 0)}, {'id':'wK' , 'pos': (4, 7)}, {'id':'wQ' , 'pos': (3, 7)},
                    {'id':'bQ' , 'pos': (3, 0)}, {'id':'bK' , 'pos': (4, 0)}]

        for x in self.board:
            for x1 in resetpos:
                if x['id'] == x1['id']:
                    a1 = (x1['pos'][0] * self.sqsz, x1['pos'][1] * self.sqsz)
                    x['pos'] = a1

    def stopmoving(self, a, b):
        if a['id'] != 'null':
            for x in self.board:
                if x['id'] == a['id']:
                    self.move(a, b)

    def move(self, a, b):
        for x in self.board:
            if x['id'] == a['id']:
                for x1 in self.board:
                    if x1['pos'] == b:
                        x1['pos'] = (-1, -1)
                x['pos'] = b
                self.moving = {'id': 'null'}
                self.moving2 = (-1, -1)

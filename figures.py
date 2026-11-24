"""figures = [{"wk":[1,5],"wq":[1,4],"wr1":[1,1],"wr2":[1,8],"wn1":[1,2],"wn2":[1,7],"wb1":[1,3],"wb2":[1,6],
            "wp1":[2,1],"wp2":[2,2],"wp3":[2,3],"wp4":[2,4],"wp5":[2,5],"wp6":[2,6],"wp7":[2,7],"wp8":[2,8]},
           {"bk":[8,5],"bq":[8,4],"br1":[8,1],"br2":[8,8],"bn1":[8,2],"bn2":[8,7],"bb1":[8,3],"bb2":[8,6],
            "bp1":[7,1],"bp2":[7,2],"bp3":[7,3],"bp4":[7,4],"bp5":[7,5],"bp6":[7,6],"bp7":[7,7],"bp8":[7,8]}]"""
class Figure:
    def __init__(self,color,alive, pos):
        self.color = color
        self.alive = alive
        self.pos = pos

    def select(self,i,j):
        if i != 0 or j != 0:
            if 1 <= self.pos[0] + i <= 8:
                if 1 <= self.pos[1] + j <= 8:
                    return [self.pos[0] + i, self.pos[1] + j]
        return 0


class King(Figure):
    def __init__(self,color,alive,pos):
        super().__init__(color,alive,pos)

    def move(self):
        dif_move = []
        for i in [0,1,-1]:
            for j in [0,1,-1]:
                if self.select(i,j) != 0:
                    dif_move.append(self.select(i, j))

        return dif_move if dif_move else 0



class Queen(Figure):
    def __init__(self,color,alive,pos):
        super().__init__(color,alive,pos)

    def move(self):
        dif_move = []
        for i in range(-7,8):
            if self.select(i, 0) != 0:
                dif_move.append(self.select(i, 0))
            if self.select(0, i) != 0:
                dif_move.append(self.select(0, i))
            if self.select(i, i) != 0:
                dif_move.append(self.select(i, i))
            if self.select(i, -i) != 0:
                dif_move.append(self.select(i, -i))

        return dif_move if dif_move else 0

class Bishop(Figure):
    def __init__(self,color,alive,pos):
        super().__init__(color,alive,pos)

    def move(self):
        dif_move = []
        for i in range(-7, 8):
            if self.select(i, i) != 0:
                dif_move.append(self.select(i, i))
            if self.select(i, -i) != 0:
                dif_move.append(self.select(i, -i))

        return dif_move if dif_move else 0

class Rook(Figure):
    def __init__(self,color,alive,pos):
        super().__init__(color,alive,pos)

    def move(self):
        dif_move = []
        for i in range(-7, 8):
            if self.select(i, 0) != 0:
                dif_move.append(self.select(i, 0))
            if self.select(0, i) != 0:
                dif_move.append(self.select(0, i))

        return dif_move if dif_move else 0

class Knight(Figure):
    def __init__(self,color,alive,pos):
        super().__init__(color, alive, pos)

    def move(self):
        dif_move = []
        for i in [-2,-1,1,2]:
            for j in [-2,-1,1,2]:
                if (i+j)%2 == 1:
                    if self.select(i, j) != 0:
                        dif_move.append(self.select(i, j))

        return dif_move if dif_move else 0

class Pawn(Figure):
    def __init__(self,color,alive,pos):
        super().__init__(color, alive, pos)

    def move(self):
        dif_move = []
        if self.color == "white":
            if self.pos[0] == 2:
                dif_move.append([self.pos[0]+2,self.pos[1]])
            for i in [-1, 0, 1]:
                if self.select(1, i) != 0:
                    dif_move.append(self.select(1, i))
        if self.color == "black":
            if self.pos[0] == 7:
                dif_move.append([self.pos[0]-2,self.pos[1]])
            for i in [-1, 0, 1]:
                if self.select(-1, i) != 0:
                    dif_move.append(self.select(-1, i))

        return dif_move if dif_move else 0




k = King("white",1,[3,5])
q = Queen("black",1,[3,5])
b = Bishop("black",1,[3,5])
r = Rook("white",1,[3,5])
n = Knight("white",1,[1,1])
p1 = Pawn("black",1,[2,1])
p2 = Pawn("black",1,[7,4])
p3 = Pawn("white",1,[2,1])
p4 = Pawn("white",1,[7,4])

print(k.move())
print(q.move())
print(b.move())
print(r.move())
print(n.move())
print(p1.move(),p2.move(),p3.move(),p4.move(),sep="\n")
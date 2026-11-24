'''figures = [{"wk":[1,5],"wq":[1,4],"wr1":[1,1],"wr2":[1,8],"wn1":[1,2],"wn2":[1,7],"wb1":[1,3],"wb2":[1,6],
            "wp1":[2,1],"wp2":[2,2],"wp3":[2,3],"wp4":[2,4],"wp5":[2,5],"wp6":[2,6],"wp7":[2,7],"wp8":[2,8]},
           {"bk":[8,5],"bq":[8,4],"br1":[8,1],"br2":[8,8],"bn1":[8,2],"bn2":[8,7],"bb1":[8,3],"bb2":[8,6],
            "bp1":[7,1],"bp2":[7,2],"bp3":[7,3],"bp4":[7,4],"bp5":[7,5],"bp6":[7,6],"bp7":[7,7],"bp8":[7,8]}]'''
class figure:
    def __init__(self,color,alive, pos):
        self.color = color
        self.alive = alive
        self.pos = pos

class king(figure):
    def __init__(self,color,alive,pos):
        super().__init__(color,alive,pos)


class queen(figure):
    def __init__(self,color,alive):
        super().__init__(color,alive)

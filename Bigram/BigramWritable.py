class Bigram:
    def __init__(self, sx, dx):
        self.sx = sx
        self.dx = dx

    def __eq__(self, other):
        return self.sx == other.sx and self.dx == other.dx

    def __hash__(self):
        return hash(self.sx) + hash(self.dx)

    def tostring(self):
        return self.sx + " " + self.dx

    def __lt__(self, other):
        return self.sx < other.sx

    def getattr(self, item):
        if item == 0:
            return self.sx
        elif item == 1:
            return self.dx
        else:
            return ValueError

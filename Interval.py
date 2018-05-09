class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[" + str(self.start) + "," + str(self.end) + "]"

    # used for print
    def __repr__(self):
        return self.__str__()
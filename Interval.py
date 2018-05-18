class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[" + str(self.start) + "," + str(self.end) + "]"

#test
if __name__=="__main__":
    tmp = Interval(3,7)
    print(tmp)

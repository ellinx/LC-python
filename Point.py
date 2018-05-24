class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        return '['+str(self.x)+','+str(self.y)+']'

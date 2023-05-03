class Car:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'a {self.color} car!!'.format(self=self)

    def __repr__(self):
        rep = 'Person (' + self.color + ',' + str(self.color) + ')'
        return rep
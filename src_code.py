
class StubClass(object):
    c_number = 0

    def __init__(self):
        print "init..."

    def increase_n(self):
        self.c_number += 1
        return self.c_number


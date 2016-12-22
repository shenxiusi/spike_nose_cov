

class StubClass(object):
    c_number = 0

    def increase_n(self):
        print self.c_number
        self.c_number += 1
        print(self.c_number)
        return self.c_number



class part(object):
    def __init__(self, length):
        self.length = length
        self.cut == False

    def __eq__(self, other):
        return self.length == other.length

    def __ne__(self, other):
        return not self.__eq__(other)

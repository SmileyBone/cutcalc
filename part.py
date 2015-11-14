
class part(object):
    def __init__(self, length, needed):
        self.length = length
        self.needed = needed
        self.cut = 0

    def __lt__(self, other):
        return self.length < other.length

    def __eq__(self, other):
        if other is None:
            return False
        return self.length == other.length

    def __ne__(self, other):
        return not self.__eq__(other)

    def remaining(self):
        return self.needed - self.cut

    def pretty_print(self):
        print self.length, ":",self.needed, ":", self.cut

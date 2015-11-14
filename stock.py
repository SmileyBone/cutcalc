import part

class stock(object):
    """the stock takes a numeric length in units"""
    def __init__(self, length):
        self.start_length = length
        self.length = length
        self.cuts = []

    """cuts the stock to the given length and returns
    a new stock at the given length"""
    def cut(self, part):
        if self.length > part.length:
            self.cuts.append(part)
            self.length -= part.length
        else:
            raise ValueError("Cut length longer than remaining length")

    def get_waste(self):
        return self.length * 1.0 / self.start_length * 1.0

    def print_pattern(self):
        pattern = ""
        for c in self.cuts:
            pattern += str(c.length) + ":"
        pattern += " | " + str(self.length)
        print pattern

    def __eq__(self, other):
        if other is None:
            return False
        if self.length == other.length:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


if __name__ == "__main__":
    import unittest
    class stock_testing(unittest.TestCase):
        def test_cut(self):
            s = stock(10)
            s.cut(5)
            self.assertEqual(s.length, 10-5)

        def test_eq(self):
            s1 = stock(5)
            s2 = stock(5)
            self.assertEqual(s1, s2)

        def test_ne(self):
            s1 = stock(10)
            s2 = stock(2)
            self.assertFalse(s1 == s2)

        def test_cutlist(self):
            s = stock(15)
            cuts = [1,2,5,2,3]
            for c in cuts:
                s.cut(c)
            self.assertEqual(cuts, s.cuts)

    unittest.main()

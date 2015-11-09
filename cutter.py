
"""
during the setup the cutter will need a list of the stock to use, and a list of parts it
should end up with.

the cutter will then calculate the set of cuts that has the minimum amount of waste
and return the list of cuts and how much stock to use.

the final list should be formatted as list of stocks with the needed cuts,
and the list of scrap."""


"""the cutter class consumes a list of stock representing the source,
and a list of parts representing the cut parts."""
import stock
import part

class cutter(object):
    def __init__(self, stocks, parts):
        self.stocks = stocks #(stock, number of stock)
        self.parts = parts #(part, number of part)

    def solve(self):
        raise ValueError("not done yet")




if __name__ == "__main__":
    stocks = [(5600, -1)]
    parts = [(1380, 22), (1520, 25), (1560, 12), (1710, 14) , (1820,18), (1880, 18),
    (1930, 20), (2000, 10), (2050, 12), (2100, 14), (2140, 16), (2150, 18), (2200, 20)]

    c = cutter(stocks, parts)

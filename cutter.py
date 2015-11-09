
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
        

        self.stocks = stocks
        self.parts = parts




if __name__ == "__main__":
    print "wut"

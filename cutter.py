
"""
during the setup the cutter will need a list of the stock to use, and a list of parts it
should end up with.

the cutter will then calculate the set of cuts that has the minimum amount of waste
and return the list of cuts and how much stock to use.

the final list should be formatted as list of stocks with the needed cuts,
and the list of scrap."""


"""the cutter class consumes a list of stock representing the source,
and a list of parts representing the cut parts."""
from stock import stock
from part import part
import heapq

class cutter(object):
    def __init__(self, stocks, parts):
        self.stocks = stocks #(stock, number of stock)
        self.parts = parts #(part, number of part)
        self.patterns = [] #list of stock where the remaining length on the stock is smaller than any part length
        heapq.heapify(self.parts)

    def solve(self):
        """solve the problem with a relaxed optimality constraint."""
        while self.get_num_parts_left() > 0:
            if len(self.stocks) == 0:
                self.stocks.append(stock(5600))#add another stock if we run out
            for s in self.stocks:
                p = self.get_largest_fitting_part(s)
                if p != None:
                    p.cut += 1
                    s.cut(p)
                else:
                    self.patterns.append(s)
                    self.stocks.remove(s)

        #add all of the partially cut stocks to the patterns
        self.patterns.extend(self.stocks)

    def get_num_parts_left(self):
        parts_left = 0
        for p in self.parts:
            parts_left += p.remaining()
        return parts_left

    """return the part that minimizes stocksize - part size, return none if no part will fit"""
    def get_largest_fitting_part(self, stock):
        largest = None
        for p in self.parts:
            if p.remaining() > 0 and p.length < stock.length:
                if largest is None or p.length > largest.length:
                    largest = p
        return largest

    def get_waste(self):
        sum_waste = 0
        for p in c.patterns:
            sum_waste += p.get_waste()
        percent_waste = sum_waste / (5600*len(self.patterns)) * 100
        return percent_waste, sum_waste

if __name__ == "__main__":
    stocks = [stock(5600)] #for now assume that we have an unlimited quantitiy of stock
    parts = [part(1380, 22), part(1520, 25), part(1560, 12), part(1710, 14) , part(1820,18), part(1880, 18),
    part(1930, 20), part(2000, 10), part(2050, 12), part(2100, 14), part(2140, 16), part(2150, 18), part(2200, 20)]

    c = cutter(stocks, parts)
    c.solve()
    p_waste, s_waste = c.get_waste()

    print "percent waste: " , p_waste
    print "total waste: " , s_waste
    print "number of patterns: " , len(c.patterns)

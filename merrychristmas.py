"""
    Christmas tree
    ===============

    : copyright: (c) 2018 by Heena Kwag.
    : URL: <https://github.com/dotaitch/merrychristmas>
"""

from random import shuffle
import time

RED = "\033[1;31;m"
GREEN = "\033[1;32;m"
NC = "\033[0m"
one = "{}1{}".format(RED, NC)
zero = "{}0{}".format(GREEN, NC)

class ChristmasTree(object):
    def __init__(self, size=3, margin_left=10, margin_topbottom=5, time=1):
        self.size = size;
        self.margin_left = margin_left
        self.margin_topbottom = margin_topbottom
        self.time = time

    def __repr__(self):
        return "Merry Christmas!"

    def nTreeElem (self):
        result = 0
        for i in range(self.size):
            for j in range(3+i):
                result = result + (2*sum(range(i+1))+1+(2*j))
        return result

    def show (self):
        n_tree_elems = self.nTreeElem()
        n_ones = int(n_tree_elems/4)

        while(1):
            tree_elem = [one]*n_ones + [zero]*(n_tree_elems-n_ones)
            shuffle(tree_elem)

            print("\n"*self.margin_topbottom)

            for i in range(self.size):
                for j in range(3+i):
                    spaces = " " * (sum(range(self.size+1)) + 1 - sum(range(i+1)) - j + self.margin_left)
                    tree = ''.join(tree_elem[:2*sum(range(i+1))+1+(2*j)])
                    del tree_elem[:(2*(i+j)+1)]
                    print("{}{}".format(spaces, tree))

            n_last_elems = 3 + sum(range(self.size+1)) * 2
            half_n_last_elems = int((n_last_elems+0.5)/2)
            center = self.margin_left + half_n_last_elems
            if center < 7:
                n_spaces = center - 2
                print("\n{0}MERRY\n{0}X-MAS{1}".format(" "*n_spaces, "\n"*self.margin_topbottom))
            else:
                n_spaces = center - 7
                print("\n{}MERRY CHRISTMAS{}".format(" "*n_spaces, "\n"*self.margin_topbottom))

            time.sleep(self.time)

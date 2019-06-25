#!/usr/bin/env python

from profit_or_loss import Profit_or_loss
from sys import argv

def main(args):
    cp = int(args[1])
    sp = int(args[2])
    
    print("The cost price and selling price are %d and %d" % (cp, sp))

    myprofit = Profit_or_loss(cp, sp)
    if sp > cp:
        print("The profit percentage is ", myprofit.profit())
    elif sp < cp:
        print("The loss percentage is ", myprofit.loss())
    else:
        print("The profit is ", myprofit.neitherprofitnorloss())
if __name__ == "__main__":
    main(argv)
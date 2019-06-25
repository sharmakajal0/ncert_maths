class Profit_or_loss:
    def __init__(self, cp, sp):
        self.cp = cp
        self.sp = sp

    def profit(self):
        if self.cp < self.sp:
            p = self.sp - self.cp
            print(p)
            p = (p / self.cp ) * 100
        return p

    def loss(self):
        if self.cp > self.sp:
            l = self.cp - self.sp
            print(l)
            l = (l / self.cp) * 100
        return l
        
    def neitherprofitnorloss(self):
            return 0


            
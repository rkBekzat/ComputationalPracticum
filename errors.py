import cmath


class Error:
    def __init__(
            self,
            method,
            exact,
            c
    ):
        self.method=method
        self.exact=exact
        self.c=c

    def Calculate(self, x, X, h, sz):
        #LTE
        lte = list()
        lte.append(0)
        for i in range(sz-1):
            lc = self.method.func(x, self.exact.exact_func(x, self.c), h)
            lte.append(abs(lc - self.exact.exact_func(x + h, self.c)).real)
            x += h

        #GTE
        gte = list()
        gte.append(0)
        x = self.method.x0
        y = self.method.y0
        for i in range(sz-1):
            gte.append(abs(self.method.func(x, y, h) - self.exact.exact_func(x + h, self.c)))
            y = self.method.func(x, y, h).real
            x += h

        return [lte, gte]



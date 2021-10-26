import cmath


class Error:
    def __init__(
            self,
            method
    ):
        self.method=method


    def Calculate(self, x, X, h):
        #LTE
        lte = list()
        lte.append(0)
        sz = int((X - x + 1) // h)
        for i in range(sz-1):
            lc = self.method.func(x, self.method.y(x), h)
            lte.append(abs(lc - self.method.y(x + h)).real)
            x += h

        #GTE
        gte = list()
        gte.append(0)
        x = self.method.x0
        y = self.method.y0
        for i in range(sz-1):
            gte.append(abs(self.method.func(x, y, h) - self.method.y(x + h)))
            y = self.method.func(x, y, h).real
            x += h

        return [lte, gte]



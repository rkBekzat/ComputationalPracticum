import cmath


class Error:
    def __init__(
            self,
            exact,
            method,
            type
    ):
        self.exact=exact
        self.method=method
        self.type=type

    def func(self, x, y):
        return cmath.sqrt(y-x)/cmath.sqrt(x)+1

    def get_local(self, type, y, x, h):
        if self.type == 'Euler':
            return y+h*self.func(x, y)
        elif self.type == 'Improved Euler':
            return y + h*self.func(x+h/2, y+h*self.func(x, y)/2)
        else:
            k1 = self.func(x, y)
            k2 = self.func(x + h / 2, y + h * k1 / 2)
            k3 = self.func(x + h / 2, y + h * k2 / 2)
            k4 = self.func(x + h, y + h * k3)
            return y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6

    def LTE(self, x0, X, h):
        arr=list()
        arr.append(0)
        for i in range(1, len(self.exact)):
            lc=self.get_local(self.type, self.exact[i-1], x0, h)
            x0+=h
            arr.append(abs(lc-self.exact[i]).real)
        return arr

    def GTE(self):
        arr=list()
        for i in range(len(self.exact)):
            arr.append(abs(self.method[i]-self.exact[i]))
        return arr

    def total(self, x0, X, h):
        arr = self.LTE(x0, X, h)
        return sum(arr)
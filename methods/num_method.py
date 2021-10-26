import cmath


class equation:
    def __init__(
            self,
            name,
            x0,
            y0,
            X,
            h,
            y
    ):
        self.name=name
        self.y0=y0
        self.x0=x0
        self.X=X
        self.h=h
        self.y=y

    def y_prime(self, x, y):
        return cmath.sqrt(y-x)/cmath.sqrt(x)+1

    def func(self, x, y, h):
        return


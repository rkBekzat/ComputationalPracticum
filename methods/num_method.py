import cmath


class equation:
    def __init__(
            self,
            x0,
            y0,
            h,
    ):
        self.y0=y0
        self.x0=x0
        self.h=h


    def y_prime(self, x, y):
        return cmath.sqrt(y-x)/cmath.sqrt(x)+1

    def func(self, x, y, h):
        return


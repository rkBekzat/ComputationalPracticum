from methods.num_method import equation


class Euler(equation):
    def __init__(
            self,
            x0,
            y0,
            X,
            h,
            y,
    ):
        super(Euler, self).__init__("Euler", x0, y0, X, h, y)

    def func(self, x, y, h):
        return y+h*self.y_prime(x, y)


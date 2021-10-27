from methods.num_method import equation


class Euler(equation):
    def __init__(
            self,
            x0,
            y0,
            h,
    ):
        super(Euler, self).__init__(x0, y0, h)

    def func(self, x, y, h):
        return y+h*self.y_prime(x, y)


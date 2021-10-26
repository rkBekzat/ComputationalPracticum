from methods.num_method import equation


class ImprovedEuler(equation):

    def __init__(
            self,
            x0,
            y0,
            X,
            h,
            y,
    ):
        super(ImprovedEuler, self).__init__("Improved Euler", x0, y0, X, h, y)

    def func(self, x, y, h):
        return y + h*self.y_prime(x+h/2, y+h/2*self.y_prime(x, y))


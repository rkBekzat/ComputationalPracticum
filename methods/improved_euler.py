from methods.num_method import equation


class ImprovedEuler(equation):

    def __init__(
            self,
            x0,
            y0,
            h,
    ):
        super(ImprovedEuler, self).__init__(x0, y0, h)

    def func(self, x, y, h):
        return y + h*self.y_prime(x+h/2, y+h/2*self.y_prime(x, y))


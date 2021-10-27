from methods.num_method import equation

class  RungeKutta(equation):
    def __init__(
            self,
            x0,
            y0,
            h,
    ):
        super(RungeKutta, self).__init__(x0, y0,  h)

    def func(self, x, y, h):
        k1 = self.y_prime(x, y)
        k2 = self.y_prime(x + h / 2, y + h * k1 / 2)
        k3 = self.y_prime(x + h / 2, y + h * k2 / 2)
        k4 = self.y_prime(x + h, y + h * k3)
        return  y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6

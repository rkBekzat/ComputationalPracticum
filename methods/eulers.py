import numpy as np

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
        super(Euler, self).__init__("Euler", x0, y0, X, h, y, '-')


    def Solve(self):
        sz = int((self.X-self.x0+1)//self.h)
        arr = np.zeros(sz)
        arr[0] = self.y0
        x0=self.x0
        h=self.h
        for i in range(1, sz):
            arr[i] = arr[i-1] + h*self.y_prime(x0, arr[i-1])
            x0+=h
        return arr
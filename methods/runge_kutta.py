import numpy as np

from methods.num_method import equation


class  RungeKutta(equation):

    def __init__(
            self,
            x0,
            y0,
            X,
            h,
            y,
    ):
        super(RungeKutta, self).__init__("Runge Kutta", x0, y0, X, h, y, 'r-')

    def Solve(self):
        sz=int((self.X-self.x0+1)//self.h)
        arr = np.zeros(sz)
        arr[0] = self.y0
        x0=self.x0
        h=self.h
        for i in range(1, sz):
            k1 = self.y_prime(x0,arr[i-1])
            k2 = self.y_prime(x0+h/2, arr[i-1]+h*k1/2)
            k3 = self.y_prime(x0+h/2, arr[i-1]+h*k2/2)
            k4 = self.y_prime(x0+h, arr[i-1]+h*k3)
            arr[i] = arr[i-1] + h * (k1+2*k2+2*k3+k4)/6
            x0+=h
        return arr

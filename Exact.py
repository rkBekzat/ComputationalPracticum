import cmath
import math

from methods.runge_kutta import RungeKutta


class exactSolution:
    def __init__(self, x0, y0):
        self.x0=x0
        self.y0=y0

    def get_coef(self):
        # y=-2sqrt(x)/c + 1/c^2 + 2x
        # yc^2=-2sqrt(x)c + 1 + 2xc^2
        # (y-2x)c^2 + 2sqrt(x)c - 1 = 0
        #
        # -b+-sqrt(b^2-4ac)/2a
        #
        # (-2sqrt(x)+sqrt(4x+4(y-2x)))/2(y-2x)
        # (-2sqrt(x)-sqrt(4x+4(y-2x)))/2(y-2x)


        c1=(-2*math.sqrt(self.x0)+math.sqrt(self.x0*4+4*(self.y0-self.x0*2)))/(2*(self.y0-self.x0*2))
        c2=(-2*math.sqrt(self.x0)-math.sqrt(self.x0*4+4*(self.y0-self.x0*2)))/(2*(self.y0-self.x0*2))

        return [c1, c2]

    def choose(self):
        h=0.1
        method=RungeKutta(self.x0, self.y0, h)
        next_y=method.func(self.x0, self.y0, h) # we find y for self.x0+0.1
        coef=self.get_coef()
        dif1=next_y-self.exact_func(self.x0+h, coef[0])
        dif2=next_y-self.exact_func(self.x0+h, coef[1])
        if dif1.real > dif2.real:
            return coef[1]
        return coef[0]

    def exact_func(self, x, c):
        return -2*math.sqrt(x)/c+1/(c**2)+2*(x)
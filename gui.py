import cmath

from matplotlib import pyplot as plt

from Exact import exactSolution
from errors import Error
import numpy as np

from methods.eulers import Euler
from methods.improved_euler import ImprovedEuler
from methods.runge_kutta import RungeKutta

x_label=['X', 'X', 'X', 'N']
y_label=['Y', "LTE value", "GTE value", "Total Error"]
graphs_name=["Exact and numerical solution", "Local truncation error", "Global truncation error", "Total approximation error depending in the number of grid cell"]
names=["Euler method", "Improved Euler Method", "Runge Kutta"]



def build(x, method):
    arr=list()
    y=method.y0
    h=method.h
    arr.append(y)
    for i in x:
        arr.append(method.func(i, y, h))
        y=method.func(i, y, h)
    arr.pop()
    return arr

def plotting(title, ylabel, xlabel, x, func, names):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    for i in range(3):
        plt.plot(x[1:] if xlabel=='N' else x, func[i], label=names[i])
    plt.legend()
    plt.grid(True)

class MainWindow:
    def __init__(self, x0, y0, X, N):
        self.x0=x0
        self.y0=y0
        self.X=X
        self.N=N
        self.x=np.linspace(x0, X, N)
        self.exact_y=exactSolution(x0, y0)
        self.c=self.exact_y.choose()
        self.h=(X-x0+1)/N
        self.exact=[self.exact_y.exact_func(i, self.c) for i in self.x]
        self.methods = [Euler(x0, y0, self.h), ImprovedEuler(x0, y0, self.h), RungeKutta(x0, y0, self.h)]
        self.graphs=list()

    def calc_total(self):
        total = [list(), list(), list()]
        for i in range(2, self.N+1):
            x=np.linspace(self.x0, self.X, i)
            h=(self.X-self.x0+1)/i
            for j in range(3):
                total[j].append(max(Error(self.methods[j], self.exact_y, self.c).Calculate(self.x0, self.X, h, i)[1]))
        #print(total)
        return total

    def build_graph(self):
        self.graphs.append([build(self.x, self.methods[i]) for i in range(3)])
        self.graphs.append([Error(self.methods[i], self.exact_y, self.c).Calculate(self.x0, self.X, self.h, self.N)[0] for i in range(3)])
        self.graphs.append([Error(self.methods[i], self.exact_y, self.c).Calculate(self.x0, self.X, self.h, self.N)[1] for i in range(3)])
        self.graphs.append(self.calc_total())

    def show_graphs(self):
        for i in range(4):
            plt.figure(i)
            plotting(graphs_name[i], y_label[i], x_label[i], self.x, self.graphs[i], names)
        plt.show()



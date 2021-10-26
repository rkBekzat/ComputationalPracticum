from gui import MainWindow

def Enter_data():
    x0=int(input("enter the initial x0:"))
    y0=int(input("enter the initial y0:"))
    X=int(input("enter the finish point X:"))
    N=int(input("enter the number of points N:"))
    return [x0, y0, X, N]


x0, y0, X, N = Enter_data()
gui=MainWindow(x0, y0, X, N)
gui.build_graph()
gui.show_graphs()


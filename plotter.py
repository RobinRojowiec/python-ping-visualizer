import matplotlib.pyplot as plt
from pinging import ping
import time
import time

import matplotlib.pyplot as plt

from pinging import ping


class Plotter:
    def __init__(self):
        self.plt = plt
        self.xaxis = 100;
        self.y_max = 200
        self.plt.axis([0, self.xaxis, 0, self.y_max])

    def plot(self, x, y):
        self.xaxis += 1
        self.plt.scatter(x, y)
        self.plt.axis([0, self.xaxis, 0, self.y_max])
        self.plt.pause(0.05)


if __name__ == '__main__':
    plotter = Plotter()
    ip = "8.8.8.8"

    i = 0
    while True:
        r = ping(ip)
        plotter.plot(i, int(r))
        i += 1
        time.sleep(0.5)

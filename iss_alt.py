import requests
from itertools import count

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")

time = list()
alt = list()

c = count()


def animate(i):
    iss = requests.get("https://api.wheretheiss.at/v1/satellites/25544").json()
    time.append(next(c))
    alt.append(iss["altitude"])
    plt.cla()
    plt.plot(time, alt)


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.xlabel("time")
plt.ylabel("Altitude")

plt.tight_layout()
plt.show()

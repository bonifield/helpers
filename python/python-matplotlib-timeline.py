# derived and modified from
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/timeline.html#sphx-glr-gallery-lines-bars-and-markers-timeline-py

# python3 python-matplotlib-timeline.py

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

domains = ["domain1.example", "domain2.example", "333.333.333.333", "domain4.example", "domain5.example",
		"domain6.example", "domain7.example", "333.333.333.333", "444.444.444.444", "domain10.example"]

dates = ["2019-02-26 13:50:55", "2019-02-26 13:51:03", "2019-02-26 13:51:04", "2019-02-26 13:51:15", "2019-02-26 13:51:21",
		"2019-02-26 13:52:14", "2019-02-26 13:52:33", "2019-02-26 13:52:37", "2019-02-26 13:52:42", "2019-02-26 13:52:47"]

# Convert date strings (e.g. "2019-02-26 13:52:43") to datetime objects
dates = [datetime.strptime(d, "%Y-%m-%d %H:%M:%S") for d in dates]

# Choose some nice levels for the stems
levels = np.tile([-5, 5, -3, 3, -1, 1], int(np.ceil(len(dates)/6)))[:len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(8.8, 4), dpi=100, layout="constrained")
ax.set(title="Domain Communication")

ax.vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
ax.plot(dates, np.zeros_like(dates), "-o", color="k", markerfacecolor="w")  # Baseline and markers on it.

# annotate lines
for d, l, r in zip(dates, levels, domains):
	ax.annotate(r, xy=(d, l),
				xytext=(-3, np.sign(l)*3), textcoords="offset points",
				horizontalalignment="right",
				verticalalignment="bottom" if l > 0 else "top")

# CAUTION: show all times, even empty ones, in 2-second intervals (default ~5 units)
#ax.xaxis.set_major_locator(mdates.SecondLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# remove y-axis and spines (the graph outline which interferes with labels)
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y=0.1)
plt.show()
#plt.savefig(fname="timeline.png")

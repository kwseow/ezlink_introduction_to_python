#
import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

with open('scatter.csv') as fp:
	reader = csv.reader(fp)
	data = list()

data_x = [float(x) for x, y, in data]
data_y = [float(y) for x, y in data]

plt.scatter(data_x, data_y)




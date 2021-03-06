import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def value_format(value, position):
	return '$ {}M'.format(int(value))

VALUES = [100,150,125,170]
POS = [0,1,2,3]
LABELS = ['Q1 2018','Q2 2018','Q3 2018','Q4 2018']

plt.bar(POS,VALUES, color='xkcd:moss green')
plt.xticks(POS, LABELS)
plt.ylabel('Sales')

axes = plt.gca()
axes.yaxis.set_major_formatter(FuncFormatter(value_format))

plt.show()

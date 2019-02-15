import matplotlib.pyplot as plt

VALUESA = [100,150,125,170]
VALUESB = [0,15,40,80]


POS = [0,1,2,3]
LABELS = ['Q1 2018','Q2 2018','Q3 2018','Q4 2018']

plt.bar(POS,VALUESB)
plt.bar(POS,VALUESA,bottom=VALUESB)
plt.xticks(POS, LABELS)
plt.ylabel('Sales')
plt.xticks(POS, LABELS)

plt.show()

import matplotlib.pyplot as plt
import numpy as np
f = open('sub_class')
f1 = open('data')
x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x5 = []
y5 = []
for lines in f.readlines():
    x.append(float(lines))
i = 0
for lines in f1.readlines():
    line = lines.strip().split('\t')
    if x[i] == 1.0:
        x1.append(float(line[0]))
        y1.append(float(line[1]))
    if x[i] == 2.0:
        x2.append(float(line[0]))
        y2.append(float(line[1]))
    if x[i] == 3.0:
        x3.append(float(line[0]))
        y3.append(float(line[1]))
    if x[i] == 4.0:
        x4.append(float(line[0]))
        y4.append(float(line[1]))
    if x[i] == -1.0:
        x5.append(float(line[0]))
        y5.append(float(line[1]))
    i += 1
plt.scatter(np.array(x1),np.array(y1),marker='.')
plt.scatter(np.array(x2),np.array(y2),marker='o')
plt.scatter(np.array(x3),np.array(y3),marker='*')
plt.scatter(np.array(x4),np.array(y4),marker='^')
#噪声点
plt.scatter(np.array(x5),np.array(y5),marker='>',linewidths=5)
plt.show()
f.close()
f1.close()

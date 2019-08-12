import matplotlib.pyplot as plt
import numpy as np
f = open('data')
x1 = []
y1 = []
x2 = []
y2 = []

for line in f.readlines():
    lines = line.strip().split("\t")
    if float(lines[2]).__eq__(0):
        x1.append(float(lines[0]))
        y1.append(float(lines[1]))
    else:
        x2.append(float(lines[0]))
        y2.append(float(lines[1]))

f.close()
plt.scatter(np.array(x1),np.array(y1),label='one',marker='*')
plt.scatter(np.array(x2),np.array(y2),label='two')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.axis([-5,5,-5,3])
plt.grid(True)
plt.show()

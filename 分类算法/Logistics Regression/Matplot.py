import matplotlib.pyplot as plt
import numpy as np
f = open('data.txt')
x1 = []
y1 = []
x2 = []
y2 = []
for lines in f.readlines():
    line = lines.strip().split('\t')
    if line[2].__eq__('0'):
        x1.append(float(line[0]))
        y1.append(float(line[1]))
    else:
        x2.append(float(line[0]))
        y2.append(float(line[1]))



#print(y1)
plt.scatter(np.array(x1),np.array(y1),marker='.')
plt.scatter(np.array(x2),np.array(y2),marker='*')
#f = open('weights')
#print(type(f.read()))
#line = f.read().strip().split('\n')
#k = 1
#x = np.linspace(0,0.8,8)
#y = float(line[1]) * x + float(line[0])
#plt.plot(x,y,color='red')
#k = 0.01
#plt.axis([0,1,-1.5,1.5])
#plt.plot(np.array(x),np.array(y1))
plt.show()
f.close()

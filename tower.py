import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

#########


#with open('droptower_vdata.txt') as f:
  #  for line in f:
x,y = np.loadtxt('droptower_vdata.txt', unpack = True)
print(x)
print(y)

fig = plt.figure()
fig.suptitle('Velocity')
plt.scatter(x,y)
plt.show()
fig.savefig('velocity.jpg')

iy = integrate.cumtrapz(y, x, initial=0)

fig = plt.figure()
fig.suptitle('Position')
plt.scatter(x,iy)
plt.show()
fig.savefig('Postition.jpg')

dy = np.diff(y)

dx= np.delete(x,-1)
print(dx)

fig = plt.figure()
fig.suptitle('Acceleration')
plt.scatter(dx,dy)
plt.show()
fig.savefig('Acceleration.jpg')

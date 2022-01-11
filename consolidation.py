# Pyhon code on Consolidation FDM by sanshrit singhai

import numpy as np
import matplotlib.pyplot as plt
#initialization
n = 5  #no. of steps
m= n+1
ho = 4 # depth of clay layer
dz = ho/n
cv = 2.52  # coefficient of consolidation
t = 0.5  # time in years
dt = t/n
a = cv*dt/dz**2 # a should be less than 0.5
print(a)

# Initialization of pressure u
u = np.zeros((m,m))
# BC at top
duo=np.zeros(m) # Excess pore pressure distribution
z = np.linspace(0,m-1,m) # along z direction
for i in range(1,m):
    duo[i] = 80 - (2 * z[i]**2) # excess pore pressure distribution
    u[i, 0] = duo[i]
# FDM SOLVER
for j in range(0,n):
    for i in range(1,n):
        u[i,j+1] = u[i,j] + (a * ((u[i-1,j])- (2*u[i,j]) +(u[i+1,j])))
# BC for bottom
for j in range(0,n):
    u[n, j+1] = u[n, j] + a * (2*u[n-1, j] - 2 * u[n, j])
print(u)
# plotting
plt.plot(u[0:n,0], -z[0:n],label='1st month')
plt.plot(u[0:n,1], -z[0:n],label='2nd month')
plt.plot(u[0:n,2], -z[0:n],label='3rd month')
plt.plot(u[0:n,3], -z[0:n],label='4th month')
plt.plot(u[0:n,4], -z[0:n],label='5th month')
plt.plot(u[0:n,5], -z[0:n],label='6th month')
plt.xlabel('Excess porewater Pressure (KPa)')
plt.ylabel('Depth (m)')
plt.legend()
plt.title('Excess porewater Pressure distribution')
plt.show()
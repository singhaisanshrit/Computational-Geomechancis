import numpy as np
import matplotlib.pyplot as plt
import math
#initializing parameters
nx=200                #no. of girds
xm=200               #physical domain
dx=xm/(nx-1)         #dis. between girds
x = np.linspace(0,xm,nx+1)
c0= 500                  #initial velocity of source
dt=0.001               #per increment time
nt=200              #Time duration of propagation
err=c0*(dt/dx) # solution to converge error should be less than 1
print(err)
# Initialization
u = np.zeros((nx, nt))  # Intializing pressure
f = np.zeros(nx)        # bc1 u at time 0
phi = np.zeros(nx)      #
alpha = err
k = dt
time = np.linspace(0 * dt, nt * dt, nt)
for i in range(0, nx):
    f[i] = math.sin(x[i])  # Input function at time 0
    phi[i] =-1* math.cos(x[i])
    u[i,0] = f[i]        # initial condition

phi1 = 10   # dominant frequence on right
phi2 = 0    # frequence on left
w2 = np.zeros(nx)
w3 = np.zeros(nx)
w2[0] = phi1
w3[nx - 1] = phi2
w1 = np.identity(nx) * (1 - alpha ** 2)
A = np.identity(nt) * 2 * (1 - alpha) ** 2
ide = np.ones(nx)

u1 = np.zeros(nx * nt)
for i in range(0, nx):
    for j in range(0, nx):
        if j == i + 1:
            w1[i, j] = alpha ** 2 / 2

for i in range(0, nt):
    for j in range(0, nt):
        if j == i + 1:
            A[i, j] = alpha ** 2
#finite difference formulation
ide1= np.identity(nx)*k
for i in range (0,nx):
    u[i,1] =  w1[i,:].dot(u[:,0]) + ide1[i,:].dot(phi[:]) + (alpha/2)*(w2[i])+ alpha/2*w3[i]
for j in range(1,nt-1):
    for i in range(1,nx-1):
        u[i,j+1] = -u[i,j-1] + A[i,j]*u[i,j] + alpha**2*(u[i+1,j]+u[i-1,j])
# plots

xx = np.linspace(0, nx, xm)
for j in range (0,nt):
    plt.plot(xx, u[:,j])
    plt.xlabel('x')
    plt.ylabel('pressure')
    plt.show()


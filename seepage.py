
import numpy as np
import matplotlib.pyplot as plt


# initialization of Domain
nx = 20  # no. of divisions along x
nx1 = nx -1
ny = 20 # no. of divisions along y
ny1 = ny - 1
b = 10 # width of domain
l = 10 # length of domain
dx = b/nx
dy = l/ny
bf = 2
b1 = 4
b2= b-(bf+b1)
nb1 = b1/dx
nb2 = b2/dx
nb11 = nb1-1
nb21 = nb2 - 1
k = 1* 10 ** -6  # permiability of soil(m/s)
h1 = 8  # head on the left (m)
h2 = 3# head on the left

# In[3]:

h = np.zeros((nx, ny)) # h is head
vx = np.zeros((nx, ny)) # v is velocity along x
# Boundary on left
a1 = nb1
a2 = (nx - nb2) - 1
itr= 1000
for i in range(0, itr):
# Boundary at top
    for i in range(0, nx):
        if i < a1:
            h[ny - 1, i] = h1
        elif i > a2:
            h[ny - 1, i] = h2
        else:
            h[nx-1, i] = h[nx-2,i]

        # Boundary on left
    for i in range(0, ny - 1):
        h[i, 0] = h[i, 1]
        # Boundary on right
    for i in range(0, ny - 1):
        h[i,ny-1] = h[i,ny-2]
        # Boundary on bottom
        for i in range(1, nx):
            h[0, i] = h[1, i]

        # Interior Nodes
    for i in range(1, ny - 1):
        for j in range(1, nx - 1):
            h[i, j] = 0.25 * (h[i + 1, j] + h[i - 1, j] + h[i, j + 1] + h[i, j - 1])

print(h)

# In[4]:

np.savetxt("head.txt", h, fmt="%s")

#Velocity flow line and discharge q
for i in range(0,ny):
    for j in range(0,nx-1):
        vx[i,j]=(k/dx)*(h[i,j+1]-h[i,j])
print(vx)

# contour
x = np.linspace(0, b, nx)
y = np.linspace(0, l, ny)

X, Y = np.meshgrid(x, y)

Z = h
fig, ay = plt.subplots(figsize=(6, 6))

fig, ay = plt.subplots(figsize=(6, 6))

ay.contour(X, Y, vx)
ay.contour(X,Y,h)

plt.show()


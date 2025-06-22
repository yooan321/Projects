import numpy as np
import matplotlib.pyplot as plt

dt = 0.1, 0.05, 0.025, 0.0125, 0.00625
t = np.arange(0,0.5 + dt[0], dt[0])
dx = 0.1
x = np.arange(0,1+dx,dx)
boundcon = [0,0]
initialcon = np.sin(np.pi*x)

n = len(x)
m = len(t)
T =  np.zeros((n,m))
T[0,:] = boundcon[0]; T[-1,:] = boundcon[1]; T[:, 0] = initialcon
T[:, 1] = (initialcon - dt[0] / 2 * np.pi ** 2  * np.sin(np.pi *  x))/(1+dt[0] / 2 *  np.pi**2)
T[:, 2] = (T[:, 1] - dt[0] / 2 * np.pi ** 2  * np.sin(np.pi *  x))/(1+dt[0] / 2 *  np.pi**2)


di1 = np.ones(n)*(5*dt[0]/(6*dx**2))
di2 = np.ones(n-1)*(dt[0]/dx**2)
A = np.diag(di1) + np.diag(di2,1)

for i in range(m-3):
    T[:, i+3] = A@(3*T[:,i+2]-3/2*T[:,i+1]+1/3*T[:,i])

tru = np.zeros((n, m))

for j in range(m):
    for i in range(n):
        tru[i,j] = math.exp(-math.pi**2*j)*math.sin(i)

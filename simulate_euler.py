import numpy as np

def simulate(f, x0, dt, Tmax):
    param_size = np.size(x0)
    time_duration = int(Tmax/dt)
    x = np.empty((time_duration, param_size))
    x[0, :] = x0
    for t in range(time_duration - 1):
        dx = f(x[t, :])
        x[t+1, :] = dt * dx + x[t, :]
    return x

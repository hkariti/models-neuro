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

def fitzhugh_nagumo_dx(x, I=0, a=0.7, b=0.8, epsilon=0.01):
    return np.array([x[0] - x[0]**3/3 - x[1] + I, epsilon*(x[0] + a - b*x[1])])

fitzhugh_nagumo_stable_point = (-1.2, -0.62)

def count_spikes(x, A=1.5):
    mask = x > A
    diff = mask[1:] > mask[:-1]
    spikes = diff.sum()
    if spikes > 0:
        return spikes - 1
    return 0

import numpy as np
import matplotlib.pyplot as plt

# Parameters
beta = 0.4     # infection rate
gamma = 0.3    # recovery rate
N = 20000000       # population size
I0 = 1         # initial number of infected individuals
R0 = 0         # initial number of recovered individuals
S0 = N - I0 - R0  # initial number of susceptible individuals
t_max = 365    # simulation time (days)
dt = 1/24      # time step (hours)

# Initialize
t = np.arange(0, t_max+dt, dt)
S = np.zeros_like(t)
I = np.zeros_like(t)
R = np.zeros_like(t)
S[0] = S0
I[0] = I0
R[0] = R0

for i in range(1, len(t)):
    dSdt = -beta * S[i-1] * I[i-1] / N
    dIdt = beta * S[i-1] * I[i-1] / N - gamma * I[i-1]
    dRdt = gamma * I[i-1]
    S[i] = S[i-1] + dSdt * dt
    I[i] = I[i-1] + dIdt * dt
    R[i] = R[i-1] + dRdt * dt

# Plotting
plt.plot(t, S, label='Susceptible')
plt.plot(t, I, label='Infected', color="r")
plt.plot(t, R, label='Recovered', color="g")
plt.xlabel('Time (days)')
plt.ylabel('Number of individuals')
plt.legend()
plt.show()

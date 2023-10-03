import numpy as np
import matplotlib.pyplot as plt

# Define the ODE for a simple harmonic oscillator: d^2x/dt^2 + omega^2*x = 0
def harmonic_oscillator_ode(x, t, omega):
    dxdt = [x[1], -omega**2 * x[0]]
    return dxdt

# Parameters
omega_values = [2, 0.5, 0]  # Angular frequencies for the three graphs
position_0 = 1.0  # Initial displacement
t_start = 0.0
t_end = 10.0
num_points = 1000  # Number of time points

# Create an array of time values manually
dt = (t_end - t_start) / (num_points - 1)
t = []
current_time = t_start
for _ in range(num_points):
    t.append(current_time)
    current_time += dt

# Implement the fourth-order Runge-Kutta method
def runge_kutta_4th_order(ode, position_0, t, omega):
    n = len(t)
    position = np.zeros(n)
    velocity = np.zeros(n)
    position[0] = position_0
    if omega == 0:
        velocity_0 = 1  # Set velocity_0 to 1 when omega is 0
    else:
        velocity_0 = 0
    velocity[0] = velocity_0
    for i in range(1, n):
        h = t[i] - t[i-1]
        k1 = h * np.array(ode([position[i-1], velocity[i-1]], t[i-1], omega))
        k2 = h * np.array(ode([position[i-1] + k1[0]/2, velocity[i-1] + k1[1]/2], t[i-1] + h/2, omega))
        k3 = h * np.array(ode([position[i-1] + k2[0]/2, velocity[i-1] + k2[1]/2], t[i-1] + h/2, omega))
        k4 = h * np.array(ode([position[i-1] + k3[0], velocity[i-1] + k3[1]], t[i-1] + h, omega))
        position[i] = position[i-1] + (k1[0] + 2*k2[0] + 2*k3[0] + k4[0]) / 6
        velocity[i] = velocity[i-1] + (k1[1] + 2*k2[1] + 2*k3[1] + k4[1]) / 6
    return position, velocity

# Create subplots for each value of omega
plt.figure(figsize=(12, 8))
for omega in omega_values:
    position, velocity = runge_kutta_4th_order(harmonic_oscillator_ode, position_0, t, omega)
    plt.subplot(3, 1, omega_values.index(omega) + 1)
    plt.plot(t, position, label='Position')
    plt.plot(t, velocity, label='Velocity')
    plt.xlabel('Time')
    plt.ylabel('Position/Velocity')
    plt.legend()
    plt.title(f'Simple Harmonic Oscillator Solution (omega = {omega})')
    plt.grid()

plt.tight_layout()
plt.show()


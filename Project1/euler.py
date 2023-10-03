import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the ODE for a simple harmonic oscillator: d^2x/dt^2 + omega^2*x = 0
def harmonic_oscillator_ode(x, t, omega):
    dxdt = [x[1], -omega**2 * x[0]]
    return dxdt

# Parameters
omega = 2.0  # Angular frequency (adjust as needed)
position_0 = 1.0  # Initial displacement
velocity_0 = 0.0  # Initial velocity
t_start = 0.0
t_end = 10.0
num_points = 1000  # Number of time points

# Calculate the time step
h = (t_end - t_start) / num_points

# Initialize position and velocity arrays
position_euler = [position_0]
velocity_euler = [velocity_0]

# Implement the Euler method
def euler_method(ode, position, velocity, t, omega):
    for i in range(1, num_points):
        t_current = t[i-1]
        dxdt = np.array(ode([position[-1], velocity[-1]], t_current, omega))
        new_position = position[-1] + h * dxdt[0]
        new_velocity = velocity[-1] + h * dxdt[1]
        position.append(new_position)
        velocity.append(new_velocity)
    return position, velocity

# Solve the ODE using the Euler method
t_values = [t_start + i * h for i in range(num_points)]
position_euler, velocity_euler = euler_method(harmonic_oscillator_ode, position_euler, velocity_euler, t_values, omega)

# Solve the ODE using scipy's odeint function
t_values = [t_start + i * h for i in range(num_points)]
initial_conditions = [position_0, velocity_0]
solution = odeint(harmonic_oscillator_ode, initial_conditions, t_values, args=(omega,))
position_odeint = solution[:, 0]
velocity_odeint = solution[:, 1]

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t_values, position_euler, label='Euler Method (Position)')
plt.plot(t_values, velocity_euler, label='Euler Method (Velocity)')
plt.plot(t_values, position_odeint, label='odeint (Position)')
plt.plot(t_values, velocity_odeint, label='odeint (Velocity)')
plt.xlabel('Time')
plt.ylabel('Position/Velocity')
plt.legend()
plt.title('Simple Harmonic Oscillator Solution Euler and SciPy')
plt.grid()
plt.show()


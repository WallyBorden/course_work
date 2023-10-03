def impulse_integral_riemann_sum(f, a, b, n):
    delta_t = (b - a) / n
    integral = 0
    for i in range(n):
        t_i = a + i * delta_t
        integral += f(t_i) * delta_t
    return integral

# Define the force equation as a function of t
def force_equation(t):
    return 3 * t**2 - t / 2 + 2

# Integration limits
a = 0
b = 3

# Number of subintervals
n = 1000  # You can adjust this value for accuracy

result_riemann = impulse_integral_riemann_sum(force_equation, a, b, n)
print("Riemann Sum Result:", result_riemann)


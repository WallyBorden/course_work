from scipy.integrate import quad

# Function to calculate the impulse using Simpson's rule
def impulse_integral_simpson(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("Number of subintervals (n) must be even for Simpson's rule.")

    delta_t = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        t_i = a + i * delta_t
        coefficient = 4 if i % 2 == 1 else 2
        integral += coefficient * f(t_i)

    integral *= delta_t / 3
    return integral

# Define the force equation as a function of t
def force_equation(t):
    return 3 * t**2 - t / 2 + 2

# Integration limits
a = 0
b = 3

# Number of subintervals (must be even)
n = 1000  # You can adjust this value for accuracy

# Compute the integral using Simpson's rule
result_simpson = impulse_integral_simpson(force_equation, a, b, n)
print("Simpson's Rule Result:", result_simpson)

# Compute the integral using SciPy's quad function
result_quad, _ = quad(force_equation, a, b)
print("SciPy quad Result:", result_quad)


from scipy.integrate import quad

# Function to calculate the impulse using the trapezoid rule
def impulse_integral_trapezoid(f, a, b, n):
    delta_t = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        t_i = a + i * delta_t
        integral += f(t_i)
    
    integral *= delta_t
    return integral

# Define the force equation as a function of t
def force_equation(t):
    return 3 * t**2 - t / 2 + 2

# Integration limits
a = 0
b = 3

# Number of subintervals
n = 1000  # You can adjust this value for accuracy

# Compute the integral using the trapezoid rule
result_trapezoid = impulse_integral_trapezoid(force_equation, a, b, n)
print("Trapezoid Rule Result:", result_trapezoid)

# Compute the integral using SciPy's quad function
result_quad, _ = quad(force_equation, a, b)
print("SciPy quad Result:", result_quad)



import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve, Eq

# Define the symbols
x = symbols('x')

# Define the coefficients of the polynomial
a, b, c, d = 1, -6, 11, -6  # Example: x^3 - 6x^2 + 11x - 6

# Define the polynomial
polynomial = a*x**3 + b*x**2 + c*x + d

# Solve for the roots
roots = solve(Eq(polynomial, 0), x)

# Convert roots to numerical values
roots_numeric = [float(root.evalf()) for root in roots]

# Define a function to evaluate the polynomial
def f(x_val):
    return a*x_val**3 + b*x_val**2 + c*x_val + d

# Generate x values for plotting
x_vals = np.linspace(min(roots_numeric) - 1, max(roots_numeric) + 1, 400)
y_vals = f(x_vals)

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = x^3 - 6x^2 + 11x - 6')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')

# Plot the roots
for root in roots_numeric:
    plt.plot(root, 0, 'ro')  # Mark the roots
    plt.annotate(f'Root: {root:.2f}', (root, 0), textcoords="offset points", xytext=(-15,10), ha='center')

# Annotate the mathematical expression
expression_text = r'$f(x) = x^3 - 6x^2 + 11x - 6$'
plt.text(0.5, 0.9, expression_text, fontsize=12, transform=plt.gca().transAxes)

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the Polynomial and its Roots')
plt.legend()

# Save the plot
plt.savefig('polynomial_roots.png')
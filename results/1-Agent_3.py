import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve, latex

# Define the symbols
x = symbols('x')

# Define the coefficients of the polynomial
a, b, c, d = 1, -6, 11, -6  # Example: x^3 - 6x^2 + 11x - 6

# Define the polynomial
polynomial = a*x**3 + b*x**2 + c*x + d

# Solve for the roots
roots = solve(polynomial, x)

# Convert roots to numerical values
roots_numeric = [float(root.evalf()) for root in roots]

# Create a function to evaluate the polynomial
def evaluate_polynomial(x_val):
    return a*x_val**3 + b*x_val**2 + c*x_val + d

# Generate x values for plotting
x_values = np.linspace(min(roots_numeric) - 1, max(roots_numeric) + 1, 400)
y_values = evaluate_polynomial(x_values)

# Plot the polynomial
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Polynomial $f(x) = x^3 - 6x^2 + 11x - 6$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')

# Plot the roots
for root in roots_numeric:
    plt.plot(root, 0, 'ro')  # Mark the roots
    plt.annotate(f'Root: {root:.2f}', (root, 0), textcoords="offset points", xytext=(-15,10), ha='center')

# Annotate the mathematical expression
expression_text = f'$f(x) = {latex(polynomial)}$'
plt.text(0.05, 0.95, expression_text, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the Polynomial and its Roots')
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('polynomial_roots_plot.png')
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbols for a general cubic: a*x^3 + b*x^2 + c*x + d = 0
a, b, c, d, x = sp.symbols('a b c d x')
general_poly = a*x**3 + b*x**2 + c*x + d

# Derive the general expression for the roots using sympy's solve function
general_roots = sp.solve(general_poly, x)
# Simplify the expressions
general_roots = [sp.simplify(root) for root in general_roots]

# Print the derived mathematical expressions for the roots
print("General expression for the roots of a cubic polynomial a*x^3 + b*x^2 + c*x + d = 0:")
for idx, expr in enumerate(general_roots, start=1):
    print(f"Root {idx} =", expr)

# Define a sample cubic polynomial: f(x) = x^3 - 6*x^2 + 11*x - 6
# Its coefficients are: a = 1, b = -6, c = 11, d = -6
sample_a = 1
sample_b = -6
sample_c = 11
sample_d = -6
sample_poly = sample_a*x**3 + sample_b*x**2 + sample_c*x + sample_d

# Compute the roots for the sample polynomial symbolically and convert to numerical values
sample_roots = sp.solve(sample_poly, x)
sample_roots = [sp.N(root) for root in sample_roots]
print("\nRoots for the sample polynomial f(x) = x^3 - 6*x^2 + 11*x - 6:")
for idx, root in enumerate(sample_roots, start=1):
    print(f"Root {idx} =", root)

# Create a numerical function for the sample polynomial using lambdify
f = sp.lambdify(x, sample_poly, 'numpy')

# Set up a range for x values, covering a little extra beyond the extreme roots
roots_float = [float(root) for root in sample_roots]
x_start = min(roots_float) - 2
x_end = max(roots_float) + 2
x_vals = np.linspace(x_start, x_end, 400)
y_vals = f(x_vals)

# Plot the sample polynomial function
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='f(x) = x^3 - 6x^2 + 11x - 6', color='blue')

# Mark the roots on the plot
plt.scatter(roots_float, f(np.array(roots_float)), color='red', zorder=5, label='Roots')

# Annotate each root on the plot
for r in roots_float:
    plt.annotate(f'{r:.2f}', (r, f(r)), textcoords="offset points", xytext=(0,10), ha='center', color='red')

# Create an annotation text for the general expression using LaTeX formatting.
# Each root is enclosed within $...$ for math rendering.
general_expr_lines = []
for i, expr in enumerate(general_roots):
    # Use LaTeX formatting for each root
    general_expr_lines.append(f"$R_{{{i+1}}} = {sp.latex(expr)}$")
general_expr_annotation = "General Cubic Roots:\n" + "\n".join(general_expr_lines)
plt.text(0.05, 0.95, general_expr_annotation, transform=plt.gca().transAxes,
         fontsize=8, verticalalignment='top',
         bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

plt.axhline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Cubic Polynomial and Its Roots')
plt.legend()
plt.grid(True)

# Save the plot, do not display it
plt.savefig("cubic_roots.png", bbox_inches='tight')
plt.close()
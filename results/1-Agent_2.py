import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define symbolic variables for the general cubic equation: a*x^3 + b*x^2 + c*x + d = 0
a, b, c, d, x = sp.symbols('a b c d x')
polynomial = a*x**3 + b*x**2 + c*x + d

# Solve the cubic symbolically using sympy (this produces the general Cardano‐form expressions)
roots_symbolic = sp.solve(polynomial, x)
roots_simplified = [sp.simplify(root) for root in roots_symbolic]

print("General expression for the roots of a cubic polynomial (Cardano's formula):")
for expr in roots_simplified:
    sp.pretty_print(expr)
    print()  # blank line for separation

# For a concrete example, use the sample polynomial:
# f(x) = x^3 - 6*x^2 + 11*x - 6
# which factors as (x-1)(x-2)(x-3)
a_val = 1
b_val = -6
c_val = 11
d_val = -6

# Define the sample polynomial function
def f(x_value):
    return a_val * x_value**3 + b_val * x_value**2 + c_val * x_value + d_val

# Compute the roots numerically using sympy for the sample polynomial
sample_poly = sp.Poly(x**3 - 6*x**2 + 11*x - 6, x)
sample_roots = sp.nroots(sample_poly)
# Convert sympy roots to Python complex numbers
sample_roots = [complex(root) for root in sample_roots]

print("Computed roots for the sample polynomial f(x) = x^3 - 6*x^2 + 11*x - 6:")
for r in sample_roots:
    print(r)

# Prepare data for plotting the function
x_vals = np.linspace(0, 4, 400)
y_vals = f(x_vals)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='f(x) = x^3 - 6x^2 + 11x - 6')

# Mark the real roots on the plot (ignore small imaginary parts)
for r in sample_roots:
    if abs(r.imag) < 1e-8:
        real_part = r.real
        plt.plot(real_part, f(real_part), 'ro')
        plt.annotate(f'{real_part:.2f}', (real_part, f(real_part)), textcoords="offset points", xytext=(0,10), ha='center')

# Annotate the plot with the general expression (Cardano's formula)
# After a change of variable x = t - b/(3a), the depressed cubic becomes t^3 + p*t + q = 0.
# Its solution, in terms of p and q, is:
# x = cube_root(-q/2 + sqrt((q/2)**2+(p/3)**3)) + cube_root(-q/2 - sqrt((q/2)**2+(p/3)**3)) - b/(3a)
formula_text = ("x = ∛(-q/2 + √((q/2)²+(p/3)³)) + ∛(-q/2 - √((q/2)²+(p/3)³))\n"
                "         - b/(3a)")
plt.text(0.05, 0.95, formula_text, transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Cubic Function and its Roots')
plt.legend()
plt.grid(True)

# Save the plot to a file
plt.savefig('cubic_plot.png')
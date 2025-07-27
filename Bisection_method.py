import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# Scalar version for bisection
def f(x):
    return 3 * x - math.cos(x) - 1

# Numpy version for plotting
def f_np(x):
    return 3 * x - np.cos(x) - 1

# Bisection Method
def bisection(a, b, t):
    if f(a) * f(b) >= 0:
        print("Please change values of a and b (f(a)*f(b) should be < 0)")
        return None

    step = 1
    while (b - a) / 2 > t:
        c = (a + b) / 2
        print(f"Step {step}:   a = {a:.4f},  b = {b:.4f},  c = {c:.4f},  f(c) = {f(c):.4f}")
        step += 1
        if f(c) == 0:
            break
        elif f(a) * f(c) > 0:
            a = c
        else:
            b = c

    print(f"\n✅ Final Root (Approx): c = {c:.4f}")
    return c

# --- User Input ---
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
t = float(input("Enter tolerance (t): "))

# --- Run Bisection ---
root = bisection(a, b, t)

if root is not None:
    y_root = f(root)  # root y value

    # Plot function using numpy
    x = np.linspace(-10, 10, 400)
    y = f_np(x)

    df = pd.DataFrame({'x': x, 'y': y})
    ax = df.plot(x='x', y='y', title='Bisection Method Root Plot')

    # Mark the root point
    plt.scatter(root, y_root, color='blue', s=80, marker='*', label=f"Root ≈ {root:.4f}")
    plt.text(root, y_root + 1, f"({root:.4f}, {y_root:.2f})", color='blue')

    # Labels and grid
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

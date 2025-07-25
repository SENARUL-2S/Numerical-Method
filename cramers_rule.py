import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Cramer’s Rule only works when the coefficient matrix must be square (e.g., 2×2, 3×3, 4×4, etc.)
# Coefficient matrix A
A = np.array([[2, -1, 3],  # first row
              [1, 0, 1],   # 2nd row
              [3, 2, -2]]) # 3rd row

# Constant matrix B
B = np.array([5, 3, -1])

# Calculate the determinant of A
det_A = np.linalg.det(A)

if det_A == 0:
    print("No solution.")
else:
    # Replace one column at a time with B to find determinants
    A1 = A.copy()
    A1[:, 0] = B
    det_A1 = np.linalg.det(A1)

    A2 = A.copy()
    A2[:, 1] = B
    det_A2 = np.linalg.det(A2)

    A3 = A.copy()
    A3[:, 2] = B
    det_A3 = np.linalg.det(A3)

    # Apply Cramer's Rule
    x = det_A1 / det_A
    y = det_A2 / det_A
    z = det_A3 / det_A

    print(f"Solution: x = {x:.2f}, y = {y:.2f}, z = {z:.2f}")


    # Create DataFrame
    df = pd.DataFrame({
        'Variable': ['x', 'y', 'z'],
        'Value': [x, y, z]
    })

    # Plot bar chart
    plt.bar(df['Variable'], df['Value'],color=['blue','red','black'])
    plt.title('Cramers Rule Solution')
    plt.ylabel('Value')
    plt.xlabel('Variables')
    plt.show()

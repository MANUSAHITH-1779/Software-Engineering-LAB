import matplotlib.pyplot as plt
import numpy as np
# Define the quadratic function
def weather_model(x, a, b, c):
 return a * x**2 + b * x + c
# Read parameters from the file
with open('parameters.txt', 'r') as f:
 lines = f.readlines()
# Generate x values using NumPy linspace
x_values = np.linspace(-10, 10, 400)
# Create a figure for the plot
plt.figure(figsize=(10, 6))
# Loop through each line in the file to extract parameters
for line in lines:
 x_specific, a, b, c = map(float, line.split())
 # Calculate y values for the entire range of x values
 y_values = weather_model(x_values, a, b, c)
 # Calculate y value for the specific x value
 y_specific = weather_model(x_specific, a, b, c)
 # Plot the quadratic function for the entire range
 plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c}')
 # Plot the specific point in red
 plt.plot(x_specific, y_specific, 'ro')
# Adding labels and title to the plot
plt.title('Quadratic Functions')
plt.xlabel('x')
plt.ylabel('y')
# Displaying the legend
plt.legend()
# Displaying the grid on the plot
plt.grid(True)
# Showing the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np
def weather_model(x, a, b, c):
 return a * x**2 + b * x + c
with open('parameters.txt', 'r') as f:
 line = f.readline()
 x_specific, a_specific, b_specific, c_specific = map(float, line.split())
x_values = np.linspace(-10, 10, 400)
y_values = weather_model(x_values, a_specific, b_specific, c_specific)
y_specific = weather_model(x_specific, a_specific, b_specific, c_specific)
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=f'{a_specific}x^2 + {b_specific}x +
{c_specific}')
plt.plot(x_specific, y_specific, 'ro', label=f'Specific Point ({x_specific},
{y_specific})')
plt.title('Quadratic Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
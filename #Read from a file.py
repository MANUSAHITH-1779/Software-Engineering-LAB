#Read from a file
import numpy as np
import matplotlib.pyplot as plt
def weather_model(x, a, b, c):
 return a * np.power(x, 2) + b * x + c
parameters = np.loadtxt('parameters.txt')
x_values = np.linspace(-10, 10, 400)
plt.figure(figsize=(10, 6))
for test in parameters:
 x, a, b, c = test
 y_values = weather_model(x_values, a, b, c)
 plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c}')
plt.title('Quadratic Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

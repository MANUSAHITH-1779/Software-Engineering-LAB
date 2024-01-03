import numpy as np
import matplotlib.pyplot as plt
def weather_model(x, a, b, c):
 return a*x**2 + b*x + c #equation
a = float(input("Enter the value of a: "))#enter the a value
b = float(input("Enter the value of b: "))#enter the b value
c = float(input("Enter the value of c: "))#enter the c value
x_values = np.linspace(-10, 10, 400)#creates a list of 400 values from x axis of -
10 to 10
y_values = weather_model(x_values, a, b, c)
x_specific = float(input("Enter the specific value of x: "))# enter the specific x
value
y_specific = weather_model(x_specific, a, b, c)
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c}')
plt.plot([x_specific], [y_specific], 'ro') #ro means r-red o-circle
plt.title('Weather Model') #plot the title
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi ,5)
plt.plot(x, np.sin(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.show()
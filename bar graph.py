import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Me", "Bob", "Jerry", "Nino"])
y = np.array([1, 8, 3, 10])

plt.title('Smartness',color='blue')
plt.bar(x,y)
plt.show()
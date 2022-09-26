import matplotlib.pylab as plt
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
data = [200, 350, 400, 180, 600, 30, 100]

plt.plot(years, data, color='red', marker = 'x', linestyle='--')
plt.title("Graph")
plt.ylabel("Data")
plt.show()
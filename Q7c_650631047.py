import matplotlib.pylab as plt
movies = ["Inception", "Wonder", "Interstellar", "The Secret \n Life of Walter Mitty", "Minions"]
num_oscars = [8, 1, 5, 0, 1]
plt.bar(range(len(movies)), num_oscars)
plt.title("My Favorite Movies")
plt.ylabel("The number of Academy Awards")
plt.xticks(range(len(movies)),movies)
plt.show()
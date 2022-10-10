# create data
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(42)
x = 10 * rng.rand(50)           # vector
y = x**2 - 1 + rng.randn(50)
plt.scatter(x, y);

# step 1 choose model
from sklearn.linear_model import LinearRegression

# step 2 choose Hyperparameter
model = LinearRegression(fit_intercept=True)
#model = LinearRegression(fit_intercept=False)
#print (model)

# step 3 arrange data into a feature matrix and target vector
X = x[:, np.newaxis] # X feature -> Matrix
print(X.shape)

# step 4 Fit the model
model.fit(X,y)
print(model.coef_)
print(model.intercept_)

# step 5 test with new data
xfit = np.linspace(-1, 11)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)
plt.plot(xfit, yfit, color='red');
print (model.predict([[4]]))

# Which hyperparameter tuning is better > Fit Intercept or Not Fit Intercept?
# Fit Intercept is better than not fit intercept because not fit intercept is not fit with data.
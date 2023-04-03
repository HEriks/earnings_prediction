import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


dataset = pd.read_csv('data/data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Training linear regression on whole dataset
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Training polynomial regression model on whole dataset
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Visualize linear regression results
# plt.scatter(X, y, color = 'red')
# plt.plot(X, lin_reg.predict(X), color = 'blue')
# plt.title('Linear Regression')
# plt.show()

print("Linear prediction:")
print(lin_reg.predict([[2022]]))

print("Polynomial prediction:")
print(lin_reg_2.predict(poly_reg.fit_transform([[2022]])))

# Visualize polynomial regression results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Polynomial Regression')
plt.show()

# pandas - working with structured data (tables, CSVs, databases)
import pandas as pd

# numpy - fast numerical calculations and handling large arrays
import numpy as np

# matplotlib - creating plots, charts and graphs
import matplotlib.pyplot as plt

# requests - for making api calls and fetching data from the interner
import requests

# scikit-learn - for implementing machine learning models and data preprocessing
from sklearn.linear_model import LinearRegression

#pandas
data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)

print(df)

#numpy
arr = np.array([1, 2, 3, 4])
print(arr * 2)

#matplotlib
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, marker="o")
plt.title("Sample Plot")
plt.show()

# requests
response = requests.get("https://api.github.com")
print(response.status_code)

#scikit-learn
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X, y)

print(model.predict([[5]]))

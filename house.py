 #Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
data = {
    'Square Footage': [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000],
    'Number of Bedrooms': [2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Number of Bathrooms': [1, 2, 2, 3, 3, 4, 4, 5, 5],
    'Price': [200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000]
}
df = pd.DataFrame(data)

# Define the features (X) and the target variable (y)
X = df[['Square Footage', 'Number of Bedrooms', 'Number of Bathrooms']]
y = df['Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-Squared: {r2:.2f}')

# Use the model to make predictions on new data
new_data = pd.DataFrame({'Square Footage': [2500], 'Number of Bedrooms': [4], 'Number of Bathrooms': [3]})
new_prediction = model.predict(new_data)
print(f'Predicted Price: ${new_prediction[0]:.2f}')

# Visualize the data and the model's predictions
plt.scatter(X_test['Square Footage'], y_test)
plt.plot(X_test['Square Footage'], y_pred)
plt.xlabel('Square Footage')
plt.ylabel('Price')
plt.title('Linear Regression Model')
plt.show()


# Scikit-learn Linear Regression and Model Evaluation

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# X = Input feature (Study Hours)
X = [[2], [3], [4], [5], [6], [7], [8], [9], [10], [11]]

# y = Target output (Marks)
y = [40, 50, 60, 70, 80, 90, 100, 110, 120, 130]


# Split data:
# 80% training
# 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create Linear Regression model
model = LinearRegression()


# Train the model
model.fit(X_train, y_train)


# Predict marks for test data
y_pred = model.predict(X_test)


# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


# Display results
print("===== TEST DATA =====")
print("X_test:", X_test)
print("Actual marks:", y_test)
print("Predicted marks:", y_pred)

print("\n===== MODEL EVALUATION =====")
print("Mean Absolute Error (MAE):", mae)
print("R2 Score:", r2)


# Predict marks for a new student
new_hours = [[12]]
new_prediction = model.predict(new_hours)

print("\n===== NEW PREDICTION =====")
print("Study Hours:", new_hours[0][0])
print("Predicted Marks:", new_prediction[0])
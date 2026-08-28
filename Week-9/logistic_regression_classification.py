# Scikit-learn - Logistic Regression Classification

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# X = Input / Feature
# Study hours
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]

# y = Output / Class
# 0 = Fail
# 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]


# Split data
# 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create Logistic Regression model
model = LogisticRegression()


# Train the model
model.fit(X_train, y_train)


# Predict classes for test data
y_pred = model.predict(X_test)


# Calculate model accuracy
accuracy = accuracy_score(y_test, y_pred)


# Display test results
print("===== TEST DATA =====")
print("X_test:", X_test)
print("Actual Result:", y_test)
print("Predicted Result:", y_pred)


# Display model evaluation
print("\n===== MODEL EVALUATION =====")
print("Accuracy:", accuracy)


# Predict a new student's result
new_hours = [[6]]

prediction = model.predict(new_hours)


# Convert numerical class into a meaningful result
if prediction[0] == 1:
    result = "Pass"
else:
    result = "Fail"


print("\n===== NEW PREDICTION =====")
print("Study Hours:", new_hours[0][0])
print("Predicted Result:", result)

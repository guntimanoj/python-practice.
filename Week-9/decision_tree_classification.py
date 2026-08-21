from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# X = Study hours
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]

# y = Result
# 0 = Fail
# 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create Decision Tree model
model = DecisionTreeClassifier(random_state=42)


# Train the model
model.fit(X_train, y_train)


# Predict test data
y_pred = model.predict(X_test)


# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)


print("===== DECISION TREE =====")
print("X_test:", X_test)
print("Actual:", y_test)
print("Predicted:", y_pred)
print("Accuracy:", accuracy)


# Predict a new student's result
new_hours = [[6]]
prediction = model.predict(new_hours)

result = "Pass" if prediction[0] == 1 else "Fail"

print("\n===== NEW PREDICTION =====")
print("Study Hours:", new_hours[0][0])
print("Predicted Result:", result)
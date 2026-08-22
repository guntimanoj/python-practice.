# Real Dataset Classification
# Logistic Regression + Model Evaluation + Visualization

import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)


# Load the real dataset
data = load_breast_cancer()

# X = Input features
# y = Target classes
X = data.data
y = data.target


# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create the model
model = LogisticRegression(max_iter=10000)


# Train the model
model.fit(X_train, y_train)


# Predict test data
y_pred = model.predict(X_test)


# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("===== MODEL EVALUATION =====")
print(f"Accuracy: {accuracy:.2%}")


# Display actual vs predicted values
print("\n===== FIRST 10 PREDICTIONS =====")

for actual, predicted in zip(y_test[:10], y_pred[:10]):
    actual_name = data.target_names[actual]
    predicted_name = data.target_names[predicted]

    print(
        f"Actual: {actual_name} | "
        f"Predicted: {predicted_name}"
    )


# Create confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("\n===== CONFUSION MATRIX =====")
print(cm)


# Visualize confusion matrix
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=data.target_names
)

display.plot()

plt.title("Breast Cancer Classification - Confusion Matrix")
plt.show()
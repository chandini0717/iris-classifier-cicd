<<<<<<< HEAD
from pathlib import Path

import joblib
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# --------------------------------------------------
# 1. Load Iris dataset
# --------------------------------------------------

iris = load_iris()

# Create DataFrame
df = pd.DataFrame(
    iris.data,
    columns=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
)

# Target column
df["target"] = iris.target

print("First 5 rows:")
print(df.head())


# --------------------------------------------------
# 2. Define input features and target
# --------------------------------------------------

X = df[
    [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
]

y = df["target"]


# --------------------------------------------------
# 3. Split dataset
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# --------------------------------------------------
# 4. Create ML model
# --------------------------------------------------

model = LogisticRegression(max_iter=200)

# Train
model.fit(X_train, y_train)


# --------------------------------------------------
# 5. Make predictions
# --------------------------------------------------

y_pred = model.predict(X_test)


# --------------------------------------------------
# 6. Evaluate model
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy:.2f}")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)


# --------------------------------------------------
# 7. Save model
# --------------------------------------------------

model_directory = Path("model")
model_directory.mkdir(exist_ok=True)

model_path = model_directory / "iris_model.pkl"

joblib.dump(
    {
        "model": model,
        "target_names": iris.target_names.tolist()
    },
    model_path
)

print(f"\nModel saved successfully at: {model_path}")
=======
# train_model.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(clf, "iris_model.pkl")
print("Model saved as iris_model.pkl")

>>>>>>> 23dc8e4c6428131b58f32313f6d0e1e6b46d52f6

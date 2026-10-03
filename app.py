<<<<<<< HEAD
import os

import joblib
import numpy as np

from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


# --------------------------------------------------
# Load trained model
# --------------------------------------------------

MODEL_PATH = "model/iris_model.pkl"

model_data = joblib.load(MODEL_PATH)

model = model_data["model"]
target_names = model_data["target_names"]


# --------------------------------------------------
# Home page
# --------------------------------------------------

=======
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained Iris model
model = joblib.load("iris_model.pkl")

# Home page
>>>>>>> 23dc8e4c6428131b58f32313f6d0e1e6b46d52f6
@app.route("/")
def home():
    return render_template("index.html")


<<<<<<< HEAD
# --------------------------------------------------
# Prediction API
# --------------------------------------------------

=======
# Prediction API
>>>>>>> 23dc8e4c6428131b58f32313f6d0e1e6b46d52f6
@app.route("/predict", methods=["POST"])
def predict():

    try:
<<<<<<< HEAD

        # Get JSON data
        data = request.get_json()

        # Extract features
        sepal_length = float(data["sepal_length"])
        sepal_width = float(data["sepal_width"])
        petal_length = float(data["petal_length"])
        petal_width = float(data["petal_width"])

        # Create input array
        input_data = np.array([
            [
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
            ]
        ])

        # Prediction
        prediction = model.predict(input_data)[0]

        # Convert prediction to class name
        predicted_class = target_names[prediction]

        return jsonify({
            "prediction": f"Iris-{predicted_class}"
        })

    except (KeyError, TypeError, ValueError) as error:

        return jsonify({
            "error": f"Invalid input: {error}"
        }), 400


# --------------------------------------------------
# Run application
# --------------------------------------------------

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
=======
        data = request.get_json()

        # Check whether features are provided
        if not data or "features" not in data:
            return jsonify({
                "error": "Please provide features."
            }), 400

        features = data["features"]

        # Iris dataset requires exactly 4 features
        if not isinstance(features, list) or len(features) != 4:
            return jsonify({
                "error": "Exactly 4 features are required."
            }), 400

        # Convert values to numbers
        features = np.array(features, dtype=float).reshape(1, -1)

        prediction = model.predict(features)[0]

        classes = {
            0: "Iris Setosa",
            1: "Iris Versicolor",
            2: "Iris Virginica"
        }

        result = classes.get(
            int(prediction),
            str(prediction)
        )

        return jsonify({
            "prediction": result
        })

    except (ValueError, TypeError):
        return jsonify({
            "error": "Features must contain valid numbers."
        }), 400

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
>>>>>>> 23dc8e4c6428131b58f32313f6d0e1e6b46d52f6
    )
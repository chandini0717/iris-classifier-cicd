from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained Iris model
model = joblib.load("iris_model.pkl")

# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    try:
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
    )
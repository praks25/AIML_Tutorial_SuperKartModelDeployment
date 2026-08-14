
# Initialize Flask app
app = Flask("SuperKart Regression Model API")

# Load the trained SuperKart model
model = joblib.load("superkart_model.joblib")

# Home route
@app.get("/")
def home():
    return jsonify({"message": "SuperKart Regression Model API is running!"})

# Prediction endpoint for a single record
@app.post("/predict")
def predict():
    data = request.get_json()

    # Expecting: {"features": [list of numeric values]}
    features = np.array(data["features"]).reshape(1, -1)

    prediction = model.predict(features)[0]

    return jsonify({"prediction": float(prediction)})

# Batch prediction endpoint
@app.post("/predict_batch")
def predict_batch():
    file = request.files["file"]

    df = pd.read_csv(file)
    predictions = model.predict(df).tolist()
    df["prediction"] = predictions

    return jsonify(df.to_dict(orient="records"))

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

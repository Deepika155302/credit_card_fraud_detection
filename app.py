from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
CORS(app)

# Load dataset
data = pd.read_csv("creditcard.csv")

# Create extra columns (simple dummy values)
# Because original dataset does not have these
data["Type"] = 0
data["Online"] = 1

# Select input features
X = data[["Time", "Amount", "Type", "Online"]]
y = data["Class"]

# Train ML model
model = LogisticRegression(max_iter=2000)
model.fit(X, y)

@app.route("/predict", methods=["POST"])
def predict():
    req_data = request.get_json()

    time = float(req_data["data"][0])
    amount = float(req_data["data"][1])
    type_ = float(req_data["data"][2])
    online = float(req_data["data"][3])

    prediction = model.predict([[time, amount, type_, online]])

    result = "Fraud 🚨" if prediction[0] == 1 else "Not Fraud ✅"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)

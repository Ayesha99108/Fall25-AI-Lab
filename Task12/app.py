from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("model_svc.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    try:
        features = [
            request.form["Company"],
            request.form["Type"],
            request.form["RAM"],
            request.form["Weight"],
        ]

        input_data = np.array(features,dtype=float).reshape(1, -1)

        prediction = model.predict(input_data)[0]

        return render_template("index.html",result=prediction)

    except Exception as e:
        return render_template("index.html",result="Error: " + str(e))

if __name__ == "__main__":
    app.run(debug=True)

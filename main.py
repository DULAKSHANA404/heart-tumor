from flask import Flask,render_template,request
from keras.models import load_model
import numpy as np
import joblib

model = load_model("models/model-080.keras")
data_class = joblib.load("models/data_scaler.pkl")
target_class = joblib.load("models/target_scaler.pkl")


app = Flask(__name__) 

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/predict",methods=['POST'])
def get_predict():
    result = request.form
    
    name = result["name"]
    sex = float(result["sex"])
    age = float(result["AGEIR"])
    tc = float(result["TC"])
    hdl =float(result["HDL"])
    smoke = float(result["smoke"])
    bpmed = float(result["BPMED"])
    diab = float(result["DIAB"])
    
    data = np.array([sex,age,tc,hdl,smoke,bpmed,diab]).reshape(1,-1)
    data = data_class.transform(data)
    predicted = model.predict(data)
    lable = target_class.inverse_transform(predicted)[0][0]
    print(lable)

    if lable >50:
        tab = f"{name},🚨 Your heart is screaming “I QUIT.” You're basically a medical disaster waiting to happen. 🔥"
        tab2 = "🚨 Your heart's basically flipping you off. Get checked. 🚨"
    elif lable>20:
        tab="Kinda sketchy. Your heart's on thin ice, buddy.💀 "
        tab2="Not terrible, not great. Your heart's halfway to flipping the bird. 💚 "
    else:
        tab=f"{name},Your heart is chill. For now ,but you still son of a bitch🍀"
        tab2 = "Try Again, You *Reckless* Human"
        

    return render_template("predict.html" ,lable=lable,tab = tab,tab2=tab2)

# 💔 Check Your Sh*t - Heart Risk Predictor

This is a brutally honest, dark-humored Flask web app that estimates your heart risk based on basic health info. Built with Python, Flask, and machine learning.


## 🔧 Features

- Input: Age, cholesterol, HDL, blood pressure med, diabetes, smoking status, etc.
- Output: Heart risk percentage with savage commentary
- Displays a cartoon heart image based on prediction
- Easy to run and host

---

## 📦 Requirements

Make sure Python 3.8+ is installed.

Then install dependencies with:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App Locally

### 💻 Using `flask run`:
```bash
# On Windows (CMD)
set FLASK_APP=main.py
set FLASK_ENV=development
flask run
```

```bash
# On macOS/Linux or Git Bash
export FLASK_APP=main.py
export FLASK_ENV=development
flask run
```

Open browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🚀 Deploy to Render (Free Hosting)

1. Push your project to GitHub
2. Go to [https://render.com](https://render.com)
3. Click **New → Web Service**
4. Connect your GitHub repo
5. Set the following:

   - **Build Command:**  
     ```bash
     pip install -r requirements.txt
     ```

   - **Start Command:**  
     ```bash
     gunicorn main:app
     ```

6. Add the following files to your root directory:

### 📄 `Procfile`
```
web: gunicorn main:app
```

### 📄 `requirements.txt` (example)
```
Flask
scikit-learn
keras
tensorflow
numpy
```

---

## 📁 Project Structure

```
.
├── main.py
├── templates/
│   └── index.html
│   └── result.html
├── static/
│   └── styles_2.css
│   └── angry_heart.png
├── model/
│   └── model.keras
│   └── scaler.pkl
├── requirements.txt
├── Procfile
└── README.md
```



## 👨‍💻 Author

Made with 💀 and 💻 by a sarcastic developer.  
Licensed under MIT.


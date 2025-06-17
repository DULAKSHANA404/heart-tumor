
# 💔Heart Risk Predictor

Built with Python, Flask, and machine learning.


## 🔧 Features

- Input: Age, cholesterol, HDL, blood pressure med, diabetes, smoking status, etc.
- Output: Heart risk percentage with savage commentary
- Displays a cartoon heart image based on prediction

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


## 📁 Project Structure

```
.
├── main.py
├── templates/
│   └── home.html
│   └── predict.html
├── static/
│   └── styles_2.css,styles.css
│   └── angry_heart.png
├── model/
│   └── model.keras
│   └── data.pkl,target.plk
├── requirements.txt
├── Procfile
└── README.md
```


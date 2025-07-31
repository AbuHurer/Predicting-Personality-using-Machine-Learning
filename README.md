# 🧠 Personality Type Predictor (Introvert / Ambivert / Extrovert)

This is an end-to-end Machine Learning project that predicts whether a person is an **Introvert**, **Ambivert**, or **Extrovert** based on behavioral and personality traits. The project includes:

- A trained ML model using Scikit-learn
- A web app interface using Streamlit
- Complete training and prediction pipeline

---

## 🚀 Features

- Train/test split on a personality traits dataset
- Preprocessing with `StandardScaler` and `LabelEncoder`
- Classification using `RandomForestClassifier`
- Interactive prediction app with **Streamlit**
- Age is collected but **excluded from prediction** as requested

---

## 🏗️ Project Structure

```
personality-predictor/
│
├── data/
│ └── personality_synthetic_dataset.csv # Dataset file
│
├── models/
│ ├── personality_classifier.pkl # Trained ML model
│ ├── scaler.pkl # StandardScaler object
│ └── label_encoder.pkl # LabelEncoder for target labels
│
├── app.py # Streamlit web app
├── train.py # Model training and saving script
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

## 🧪 Dataset Description

Each row in the dataset represents a user, with personality and behavior traits as input features.  
The target variable is one of:
- `Introvert`
- `Ambivert`
- `Extrovert`

**Features used** (29 total, excluding age):
- social_energy
- alone_time_preference
- talkativeness
- deep_reflection
- group_comfort
- party_liking
- listening_skill
- empathy
- creativity
- organization
- leadership
- risk_taking
- public_speaking_comfort
- curiosity
- routine_preference
- excitement_seeking
- friendliness
- emotional_stability
- planning
- spontaneity
- adventurousness
- reading_habit
- sports_interest
- online_social_usage
- travel_desire
- gadget_usage
- work_style_collaborative
- decision_speed
- stress_handling

---

## 📦 Installation

### 1️⃣ Clone the Repository
```
git clone https://github.com/yourusername/personality-predictor.git
cd personality-predictor
```
### 2️⃣ Create and Activate Virtual Environment
```
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```
### 3️⃣ Install Required Packages
```
pip install -r requirements.txt
```
### 🧠 Train the Model
```
python train.py
```
- This will train the model and save the following in the models/ directory:
- personality_classifier.pkl
- scaler.pkl
- label_encoder.pkl
### 🌐 Run the Web App
- Make sure you're in the project folder, then start Streamlit:
```
streamlit run app.py
```
### 🛠️ Requirements
- Listed in requirements.txt. Major ones:
- `scikit-learn`
- `pandas`
- `numpy`
- `streamlit`
- `joblib`
- Install using:
```
pip install -r requirements.txt
```
### 📸 Screenshots
- Screeshots are available in the Screenshot folder
---
### 🙋‍♂️ Author
 Mohammed Abu Hurer
AI Engineering Student | Passionate about Machine Learning, Computer Vision, and Real-World Applications 🚀
Feel free to reach out or contribute!
### 📄 License
This project is licensed under the MIT License.
### 🌟 Star this repository
If you found this helpful, give it a ⭐ on GitHub!

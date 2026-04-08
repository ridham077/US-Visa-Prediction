# 🇺🇸 US Visa Prediction System

## 📌 Overview
The US Visa Prediction System is a machine learning-based web application that predicts whether a visa application will be **Approved** or **Denied** based on applicant details.  
The goal of this project is to demonstrate end-to-end ML deployment using FastAPI and Streamlit.

---

## 🚀 Features
- Predict visa approval status in real-time
- User-friendly interface using Streamlit
- Backend powered by FastAPI
- Data preprocessing with pipelines
- Handles categorical & numerical features
- Scalable and modular code structure

---

## 🧠 Machine Learning
- Model trained on historical visa application data
- Applied preprocessing techniques:
  - Label Encoding / One-Hot Encoding
  - Feature Scaling
- Built using Scikit-learn pipeline for clean workflow

---

## 💻 Tech Stack
- Python
- Scikit-learn
- FastAPI
- Streamlit
- Pandas, NumPy

---

## 📊 Input Features
- Continent
- Education Level
- Job Experience (Yes/No)
- Requires Job Training (Yes/No)
- Number of Employees
- Prevailing Wage

---

## ⚙️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/visa-predictor.git
cd visa-predictor
python -m venv myenv
source myenv/bin/activate   # For Linux/Mac
myenv\Scripts\activate      # For Windows
pip install -r requirements.txt
uvicorn app:app --reload
streamlit run app.py

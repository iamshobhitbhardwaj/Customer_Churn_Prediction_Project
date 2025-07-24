# 📞 Customer Churn Prediction with Logistic Regression

This project builds a **machine learning model** to predict if a customer is likely to churn (leave a telecom service provider) based on their demographic and service usage patterns. The final model is deployed as a **Streamlit web application**.

---

## 📌 Problem Statement

Telecom companies lose a large portion of revenue due to customer churn. Identifying customers who are likely to leave helps in proactive retention strategies.  
This project aims to:
- Build a predictive model using **Logistic Regression**
- Create a **Streamlit app** for real-time churn prediction
- Deploy the app so non-technical teams (like customer support) can easily use it

---

## 📂 Dataset

The dataset (`customerChurn.csv`) contains customer information such as:
- **Demographics**: Gender, Senior Citizen, Partner, Dependents
- **Service Info**: Internet, Phone, Streaming services
- **Account Info**: Contract, Payment Method, Monthly & Total Charges
- **Target**: `Churn` column (`Yes`/`No`)

---

## 🧪 Steps Performed

### 1. 📥 Data Loading & Exploration
- Loaded the CSV file into a Pandas DataFrame
- Checked for null values and datatype inconsistencies
- Analyzed the target class distribution

### 2. 🧹 Data Preprocessing
- Converted `TotalCharges` to numeric and handled missing values
- Label-encoded the target column (`Churn`: Yes → 1, No → 0)
- One-hot encoded categorical features using `pd.get_dummies(drop_first=True)`
- Standardized `MonthlyCharges` and `TotalCharges`
- Split data into training and testing sets (80:20)

### 3. 🤖 Model Training
- Used **Logistic Regression** from `scikit-learn`
- Evaluated with:
  - Accuracy
  - Precision, Recall, F1 Score
  - Confusion Matrix

### 4. 🖥️ Streamlit App
- Built an interactive UI where users can input customer details
- App displays prediction result:
  > ✅ *Customer is likely to stay*  
  > ⚠️ *Customer is likely to churn*
- Used `pickle` to load the trained model

### 5. ☁️ Deployment
- Deployed using **Streamlit Cloud**
- Public link available below

---

## 📊 Model Performance

| Metric     | Value |
|------------|-------|
| Accuracy   | ~**83%** |
| Precision  | ~**70%** |
| Recall     | ~**65%** |
| F1 Score   | ~**67%** |

> *Metrics may vary slightly depending on train-test split*

---

## 🚀 How to Run the Project

### 🔧 Setup Instructions

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/customer-churn-app.git
   cd customer-churn-app

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run Streamlit app locally:
   ```bash
   streamlit run app.py

---

### 🌐 Live Demo
👉 Try the deployed app here:
https://customer-churn-prediction-st-app.streamlit.app

---

### 🛠️ Built With
- Python

- pandas, numpy, seaborn, matplotlib

- scikit-learn

- Streamlit

- pickle

---

### 📄 License
This project is licensed under the MIT License. Feel free to use, modify, and share with credit.

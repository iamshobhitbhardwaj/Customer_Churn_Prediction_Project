import numpy as np
import pickle
import streamlit as st

model = pickle.load(open('customer_churn_model.pkl', 'rb'))

st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

st.title("📞 Telecom Customer Churn Prediction")

st.markdown("Enter customer details to predict if they are likely to churn.")

gender = st.selectbox("Gender", ['Female', 'Male'])
SeniorCitizen = st.selectbox("Senior Citizen", ['No', 'Yes'])
Partner = st.selectbox("Has Partner", ['No', 'Yes'])
Dependents = st.selectbox("Has Dependents", ['No', 'Yes'])
tenure = st.slider("Tenure (in months)", 0, 72, 12)
PhoneService = st.selectbox("Phone Service", ['No', 'Yes'])
MultipleLines = st.selectbox("Multiple Lines", ['No phone service', 'No', 'Yes'])
InternetService = st.selectbox("Internet Service", ['No', 'DSL', 'Fiber optic'])
OnlineSecurity = st.selectbox("Online Security", ['No internet service', 'No', 'Yes'])
OnlineBackup = st.selectbox("Online Backup", ['No internet service', 'No', 'Yes'])
DeviceProtection = st.selectbox("Device Protection", ['No internet service', 'No', 'Yes'])
TechSupport = st.selectbox("Tech Support", ['No internet service', 'No', 'Yes'])
StreamingTV = st.selectbox("Streaming TV", ['No internet service', 'No', 'Yes'])
StreamingMovies = st.selectbox("Streaming Movies", ['No internet service', 'No', 'Yes'])
Contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
PaperlessBilling = st.selectbox("Paperless Billing", ['No', 'Yes'])
PaymentMethod = st.selectbox("Payment Method", [
    'Bank transfer (automatic)',
    'Credit card (automatic)',
    'Electronic check',
    'Mailed check'
])
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=70.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=500.0)

def encode_input():
    gender_male = 1 if gender == 'Male' else 0
    SeniorCitizen_val = 1 if SeniorCitizen == 'Yes' else 0
    Partner_Yes = 1 if Partner == 'Yes' else 0
    Dependents_Yes = 1 if Dependents == 'Yes' else 0
    PhoneService_Yes = 1 if PhoneService == 'Yes' else 0

    MultipleLines_No_phone = 1 if MultipleLines == 'No phone service' else 0
    MultipleLines_Yes = 1 if MultipleLines == 'Yes' else 0

    InternetService_DSL = 1 if InternetService == 'DSL' else 0
    InternetService_Fiber = 1 if InternetService == 'Fiber optic' else 0

    OnlineSecurity_No_int = 1 if OnlineSecurity == 'No internet service' else 0
    OnlineSecurity_Yes = 1 if OnlineSecurity == 'Yes' else 0

    OnlineBackup_No_int = 1 if OnlineBackup == 'No internet service' else 0
    OnlineBackup_Yes = 1 if OnlineBackup == 'Yes' else 0

    DeviceProtection_No_int = 1 if DeviceProtection == 'No internet service' else 0
    DeviceProtection_Yes = 1 if DeviceProtection == 'Yes' else 0

    TechSupport_No_int = 1 if TechSupport == 'No internet service' else 0
    TechSupport_Yes = 1 if TechSupport == 'Yes' else 0

    StreamingTV_No_int = 1 if StreamingTV == 'No internet service' else 0
    StreamingTV_Yes = 1 if StreamingTV == 'Yes' else 0

    StreamingMovies_No_int = 1 if StreamingMovies == 'No internet service' else 0
    StreamingMovies_Yes = 1 if StreamingMovies == 'Yes' else 0

    Contract_One = 1 if Contract == 'One year' else 0
    Contract_Two = 1 if Contract == 'Two year' else 0

    PaperlessBilling_Yes = 1 if PaperlessBilling == 'Yes' else 0

    Payment_Bank = 1 if PaymentMethod == 'Bank transfer (automatic)' else 0
    Payment_Credit = 1 if PaymentMethod == 'Credit card (automatic)' else 0
    Payment_Electronic = 1 if PaymentMethod == 'Electronic check' else 0

    # Scaled version assumed used in training
    input_features = np.array([[
        tenure,
        MonthlyCharges,
        TotalCharges,
        gender_male,
        SeniorCitizen_val,
        Partner_Yes,
        Dependents_Yes,
        PhoneService_Yes,
        MultipleLines_No_phone,
        MultipleLines_Yes,
        InternetService_DSL,
        InternetService_Fiber,
        OnlineSecurity_No_int,
        OnlineSecurity_Yes,
        OnlineBackup_No_int,
        OnlineBackup_Yes,
        DeviceProtection_No_int,
        DeviceProtection_Yes,
        TechSupport_No_int,
        TechSupport_Yes,
        StreamingTV_No_int,
        StreamingTV_Yes,
        StreamingMovies_No_int,
        StreamingMovies_Yes,
        Contract_One,
        Contract_Two,
        PaperlessBilling_Yes,
        Payment_Bank,
        Payment_Credit,
        Payment_Electronic
    ]])
    return input_features

# Prediction
if st.button("Predict Churn"):
    features = encode_input()
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    if prediction == 1:
        st.error(f"⚠️ The customer is **likely to churn**.\nChurn Probability: **{probability:.2f}**")
    else:
        st.success(f"✅ The customer is **likely to stay**.\nChurn Probability: **{probability:.2f}**")
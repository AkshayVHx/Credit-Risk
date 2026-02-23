import streamlit as st
import pickle
import numpy as np

# Load model
@st.cache_resource
def load_model():
    with open("trained_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

st.title("Credit Risk Prediction App")
st.write("Enter customer details to predict credit risk")

# ================= NUMERICAL INPUTS =================
duration_months = st.number_input("Loan Duration (months)", 1, 72, value=12)
credit_amount = st.number_input("Credit Amount", min_value=0, value=2000)
installment_rate = st.number_input("Installment Rate (%)", 1, 4, value=2)
age = st.number_input("Age", 18, 100, value=30)
residence_duration = st.number_input("Residence Duration (years)", 1, 4, value=2)
existing_credits = st.number_input("Existing Credits", 0, 4, value=1)
people_liable = st.number_input("People Liable", 1, 2, value=1)

# ================= CATEGORICAL INPUTS (ENCODED) =================
checking_account = st.selectbox(
    "Checking Account Status",
    options=[0, 1, 2, 3],
    format_func=lambda x: ["No account", "< 0", "0–200", "> 200"][x]
)

credit_history = st.selectbox(
    "Credit History",
    options=[0, 1, 2, 3, 4],
    format_func=lambda x: [
        "No credits", "All paid", "Existing paid", "Delay", "Critical"
    ][x]
)

purpose = st.selectbox(
    "Purpose",
    options=[0, 1, 2, 3, 4],
    format_func=lambda x: [
        "Car", "Furniture", "Education", "Business", "Other"
    ][x]
)

savings_account = st.selectbox(
    "Savings Account",
    options=[0, 1, 2, 3, 4],
    format_func=lambda x: [
        "No savings", "<100", "100–500", "500–1000", ">1000"
    ][x]
)

employment_duration = st.selectbox(
    "Employment Duration",
    options=[0, 1, 2, 3, 4],
    format_func=lambda x: [
        "Unemployed", "<1 year", "1–4 years", "4–7 years", ">7 years"
    ][x]
)

personal_status_sex = st.selectbox(
    "Personal Status & Sex",
    options=[0, 1, 2, 3]
)

guarantor = st.selectbox("Guarantor", options=[0, 1, 2])
property = st.selectbox("Property", options=[0, 1, 2, 3])
other_credits = st.selectbox("Other Credits", options=[0, 1, 2])
housing = st.selectbox("Housing", options=[0, 1, 2])
job = st.selectbox("Job", options=[0, 1, 2, 3])
telephone = st.selectbox("Telephone", options=[0, 1])
foreign_worker = st.selectbox("Foreign Worker", options=[0, 1])

# ================= PREDICTION =================
if st.button("Predict Credit Risk"):

    # ORDER MUST MATCH X_train EXACTLY
    features = np.array([[
        checking_account,
        duration_months,
        credit_history,
        purpose,
        credit_amount,
        savings_account,
        employment_duration,
        installment_rate,
        personal_status_sex,
        guarantor,
        residence_duration,
        property,
        age,
        other_credits,
        housing,
        existing_credits,
        job,
        people_liable,
        telephone,
        foreign_worker
    ]])

    prediction = model.predict(features)

    st.subheader("Result:")
    if prediction[0] == 1:
        st.error("High Credit Risk ❌")
    else:
        st.success("Low Credit Risk ✅")
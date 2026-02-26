import streamlit as st
import pickle
import numpy as np

def load_model():
    with open("trained_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

CHECKING_ACCOUNT_LABELS = [
    "No checking account",
    "< 0 DM",
    "0–200 DM",
    "≥ 200 DM / salary ≥ 1 year"
]

CREDIT_HISTORY_LABELS = [
    "Delay in paying off in the past",
    "Critical account / other credits elsewhere",
    "No credits / all paid back duly",
    "Existing credits paid back duly",
    "All credits at this bank paid back duly"
]

PURPOSE_LABELS = [
    "Other",
    "Car (new)",
    "Car (used)",
    "Furniture / equipment",
    "Radio / television",
    "Domestic appliances",
    "Repairs",
    "Education",
    "Vacation",
    "Retraining",
    "Business"
]

SAVINGS_LABELS = [
    "Unknown / no savings",
    "< 100 DM",
    "100–500 DM",
    "500–1000 DM",
    "≥ 1000 DM"
]

EMPLOYMENT_LABELS = [
    "Unemployed",
    "< 1 year",
    "1–4 years",
    "4–7 years",
    "≥ 7 years"
]

INSTALLMENT_LABELS = [
    "≥ 35%",
    "25% – <35%",
    "20% – <25%",
    "< 20%"
]

PERSONAL_STATUS_LABELS = [
    "Male: divorced/separated",
    "Female: non-single / Male: single",
    "Male: married/widowed",
    "Female: single"
]

GUARANTOR_LABELS = ["None", "Co-applicant", "Guarantor"]

RESIDENCE_LABELS = [
    "< 1 year",
    "1–4 years",
    "4–7 years",
    "≥ 7 years"
]

PROPERTY_LABELS = [
    "Unknown / no property",
    "Car or other",
    "Building savings / life insurance",
    "Real estate"
]

OTHER_CREDITS_LABELS = ["Bank", "Stores", "None"]

HOUSING_LABELS = ["For free", "Rent", "Own"]

EXISTING_CREDITS_LABELS = ["1", "2–3", "4–5", "≥ 6"]

JOB_LABELS = [
    "Unemployed / unskilled (non-resident)",
    "Unskilled (resident)",
    "Skilled employee / official",
    "Manager / self-employed / highly qualified"
]

PEOPLE_LIABLE_LABELS = ["3 or more", "0–2"]

TELEPHONE_LABELS = ["No", "Yes"]

FOREIGN_WORKER_LABELS = ["Yes", "No"]


st.title("Credit Risk Prediction App")
st.write("Enter customer details to predict credit risk")


duration_months = st.number_input("Loan Duration (months)", 1, 72, 12)
credit_amount = st.number_input("Credit Amount (DM)", min_value=0, value=2000)
age = st.number_input("Age", 18, 100, 30)


checking_account = st.selectbox(
    "Checking Account Status",
    options=range(1, 5),
    format_func=lambda i: CHECKING_ACCOUNT_LABELS[i - 1]
)

credit_history = st.selectbox(
    "Credit History",
    options=range(5),
    format_func=lambda i: CREDIT_HISTORY_LABELS[i]
)

purpose = st.selectbox(
    "Purpose of Credit",
    options=range(11),
    format_func=lambda i: PURPOSE_LABELS[i]
)

savings_account = st.selectbox(
    "Savings Account",
    options=range(1, 6),
    format_func=lambda i: SAVINGS_LABELS[i - 1]
)

employment_duration = st.selectbox(
    "Employment Duration",
    options=range(1, 6),
    format_func=lambda i: EMPLOYMENT_LABELS[i - 1]
)

installment_rate = st.selectbox(
    "Installment Rate Category",
    options=range(1, 5),
    format_func=lambda i: INSTALLMENT_LABELS[i - 1]
)

personal_status_sex = st.selectbox(
    "Personal Status & Sex",
    options=range(1, 5),
    format_func=lambda i: PERSONAL_STATUS_LABELS[i - 1]
)

guarantor = st.selectbox(
    "Other Debtors / Guarantor",
    options=range(1, 4),
    format_func=lambda i: GUARANTOR_LABELS[i - 1]
)

residence_duration = st.selectbox(
    "Present Residence Duration",
    options=range(1, 5),
    format_func=lambda i: RESIDENCE_LABELS[i - 1]
)

property_ = st.selectbox(
    "Property",
    options=range(1, 5),
    format_func=lambda i: PROPERTY_LABELS[i - 1]
)

other_credits = st.selectbox(
    "Other Installment Plans",
    options=range(1, 4),
    format_func=lambda i: OTHER_CREDITS_LABELS[i - 1]
)

housing = st.selectbox(
    "Housing",
    options=range(1, 4),
    format_func=lambda i: HOUSING_LABELS[i - 1]
)

existing_credits = st.selectbox(
    "Number of Existing Credits",
    options=range(1, 5),
    format_func=lambda i: EXISTING_CREDITS_LABELS[i - 1]
)

job = st.selectbox(
    "Job",
    options=range(1, 5),
    format_func=lambda i: JOB_LABELS[i - 1]
)

people_liable = st.selectbox(
    "People Liable for Maintenance",
    options=range(1, 3),
    format_func=lambda i: PEOPLE_LIABLE_LABELS[i - 1]
)

telephone = st.selectbox(
    "Telephone (under customer name)",
    options=range(1, 3),
    format_func=lambda i: TELEPHONE_LABELS[i - 1]
)

foreign_worker = st.selectbox(
    "Foreign Worker",
    options=range(1, 3),
    format_func=lambda i: FOREIGN_WORKER_LABELS[i - 1]
)


if st.button("Predict Credit Risk"):

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
        property_,
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

    st.subheader("Prediction Result")


    if prediction[0] == 0:
        st.error("High Credit Risk ❌")
    else:
        st.success("Low Credit Risk ✅")









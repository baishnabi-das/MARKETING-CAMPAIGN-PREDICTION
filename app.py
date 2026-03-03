import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.title("📊 Marketing Campaign Prediction")
st.write("Enter customer details (encoded numeric values)")

st.subheader("Input Features")

# IMPORTANT:
# Number of inputs = number of columns in X (df.iloc[:, :-1])
# Adjust this list ONLY if your dataset has different columns

age = st.number_input("Age", min_value=18, max_value=100)
job = st.number_input("Job (Encoded)", min_value=0)
marital = st.number_input("Marital Status (Encoded)", min_value=0)
education = st.number_input("Education (Encoded)", min_value=0)
default = st.number_input("Default Credit (Encoded)", min_value=0)
balance = st.number_input("Account Balance")
housing = st.number_input("Housing Loan (Encoded)", min_value=0)
loan = st.number_input("Personal Loan (Encoded)", min_value=0)
contact = st.number_input("Contact Type (Encoded)", min_value=0)
day = st.number_input("Day")
month = st.number_input("Month (Encoded)", min_value=0)
duration = st.number_input("Call Duration")
campaign = st.number_input("Campaign Contacts")
pdays = st.number_input("Previous Days Contacted")
previous = st.number_input("Previous Contacts")
poutcome = st.number_input("Previous Outcome (Encoded)", min_value=0)

# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame([[
        age, job, marital, education, default, balance,
        housing, loan, contact, day, month,
        duration, campaign, pdays, previous, poutcome
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Customer WILL subscribe to the campaign")
    else:
        st.error("❌ Customer will NOT subscribe to the campaign")
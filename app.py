import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("credit_model.pkl")

st.title("Credit Risk Prediction App")

# User input
def user_input():
    age = st.number_input('Age', min_value=18, max_value=100, value=30)
    sex = st.selectbox('Sex', [0, 1])  # 0: female, 1: male (or vice versa, based on your data)
    job = st.selectbox('Job', [0, 1, 2, 3])
    housing = st.selectbox('Housing', [0, 1, 2])
    saving = st.selectbox('Saving accounts', [0, 1, 2, 3, 4])
    checking = st.selectbox('Checking account', [0, 1, 2, 3])
    credit_amount = st.number_input('Credit amount', value=1000)
    duration = st.number_input('Duration (months)', value=12)
    purpose = st.selectbox('Purpose', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    data = {
        'Age': age,
        'Sex': sex,
        'Job': job,
        'Housing': housing,
        'Saving accounts': saving,
        'Checking account': checking,
        'Credit amount': credit_amount,
        'Duration': duration,
        'Purpose': purpose
    }

    return pd.DataFrame([data])

input_df = user_input()

if st.button('Predict Credit Risk'):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.error('❌High Credit Risk, Bad customer')
    else:
        st.success('✅ Low Credit Risk, Good customer')

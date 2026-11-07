import streamlit as st
import joblib

@st.cache_resource
def load_files():
    return joblib.load("sqli_model.pkl"), joblib.load("vectorizer.pkl")

model, vectorizer = load_files()

st.title("SQL Injection Detector")
st.write("Type or paste an input string. The model estimates how likely it is to be an SQL injection attempt.")

query = st.text_input("Input string:")

if query:
    prob = model.predict_proba(vectorizer.transform([query]))[0][1]
    if prob >= 0.5:
        st.error(f"Likely malicious (malicious score: {prob:.0%})")
    else:
        st.success(f"Looks benign (malicious score: {prob:.0%})")

st.caption("Educational project. Real applications should use parameterized queries as their primary defence.")
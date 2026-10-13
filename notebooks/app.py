
import pickle
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "model.pkl", "rb") as f:
    model = pickle.load(f)

with open(BASE_DIR / "vectorizer.pkl", "rb") as f:
    cv = pickle.load(f)

st.title("🌍 Language Detection App")
st.write("Enter a sentence to detect its language.")

user_input = st.text_input("Enter your text")

if st.button("Detect Language"):
    if user_input.strip():
        transformed_text = cv.transform([user_input])
        prediction = model.predict(transformed_text)
        st.success(f"Predicted language: {prediction[0]}")
    else:
        st.warning("Please enter some text.")

import streamlit as st

st.title("🌐 Multilingual Document Assistant")

st.write("My RAG application is working!")

st.success("Application ready!")

import streamlit as st
import google.generativeai as genai

API_KEY = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=API_KEY)

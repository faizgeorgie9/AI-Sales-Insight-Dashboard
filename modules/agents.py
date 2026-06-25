import google.generativeai as genai
import streamlit as st

genai.configure(
    api_key= st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_insight(question, df):

    context = df.to_string()

    prompt = f"""

    Anda adalah Business Analyst.

    Berikut data penjualan:

    {context}

    Jawablah pertanyaan berikut berdasarkan data tersebut:

    {question}

    Berikan jawaban yang singkat dan mudah dipahami oleh manajemen.

    """

    response = model.generate_content(prompt)

    return response.text

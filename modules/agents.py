import google.generativeai as genai

genai.configure(
    api_key="AIzaSyAPxvch9xfIuGiNXPK1vVb59Ck9_zY9vI4"
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

import pdfplumber
import google.generativeai as genai

genai.configure(api_key="YOUR API KEY")

def extract_text_from_pdf(file) -> str:
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def ask_gemini(question: str, context: str) -> str:
    prompt = f"Context:\n{context}\n\nQuestion:\n{question}\nAnswer:"
    model = genai.GenerativeModel('gemini-2.5-flash')  # or your correct model
    response = model.generate_content(prompt)
    return response.text if hasattr(response, 'text') else str(response)

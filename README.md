AI PDF Chatbot with Gemini
An interactive PDF chatbot application built with Streamlit and Google Gemini AI. This tool allows users to upload PDF documents, extract their content, and chat with an AI model that answers questions using both context from the PDF and generative intelligence.

Features
PDF Upload: Instantly extract text from any PDF.

Gemini AI Chat: Ask questions about the PDF and receive intelligent answers.

Session Chat History: Conversation history displayed for each session.

Modern Streamlit UI: Fast refresh, clean interface, and simple deployment.


Setup & Installation
Clone this repository:

bash
git clone <your-repo-url>
cd <repo-folder>
Set up Python environment (recommended):

bash
python -m venv venv
source venv/bin/activate   # On Windows: .\venv\Scripts\activate
Install requirements:

bash
pip install -r requirements.txt
Set API Key for Google Gemini:

Get your Gemini API key from Google AI Studio.

Add the API key in utils.py:

python
genai.configure(api_key="YOUR_API_KEY")
Run the Streamlit app:

bash
streamlit run app.py

Folder Structure
text
streamlit_pdf_chatbot/
├── app.py             # Main application UI and logic
├── utils.py           # PDF extraction and Gemini call utilities
├── requirements.txt   # List of dependencies
└── README.md          # Project documentation


Usage
Upload a PDF file using the UI.

Ask questions about the document.

View responses and chat history instantly.

Dependencies
See requirements.txt for all packages. Key dependencies include:

streamlit

pdfplumber

google-generativeai

Troubleshooting
Ensure your Python environment matches the location of installed packages.

Use Streamlit v1.33+ for best results (st.rerun() available).

Replace old model names with the latest versions (e.g., 'gemini-1.5-pro').

Always store your API key securely.

License
This project is for educational and demonstration purposes.


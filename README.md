This application is hosted on Render and is accessible at:
https://pdf-chat-application.onrender.com/

Dependencies
This project uses the following Python libraries, which are listed in the requirements.txt file:

openai==0.28.0: For interacting with OpenAI's GPT models.
langchain==0.0.154: For building the LLM-powered chatbot and managing embeddings.
PyPDF2==3.0.1: For reading and extracting text from PDF files.
python-dotenv==1.0.0: For managing environment variables securely.
streamlit==1.18.1: For building the web-based user interface.
faiss-cpu==1.7.4: For efficient similarity search and vector storage.
pydantic==1.10.9: For data validation and settings management.
altair==4.2.2: For creating visualizations (used internally by Streamlit).
tiktoken==0.4.0: For tokenization, required by OpenAI embeddings.

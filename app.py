import streamlit as st
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
# from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import os
def add_vertical_space(num_lines: int):
    for _ in range(num_lines):
        st.write("")

#Sidebar contents
with st.sidebar:
    st.title(' PDF Chat App')
    st.markdown(''' 
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
    ''')
    add_vertical_space(5)
    st.write('Made by Suvardhan Dileep Gaddameedi')

load_dotenv()
def main():
    st.header("Chat with PDF")
    
    

    #upload a PDF file
    pdf=st.file_uploader("Upload your PDF",type='pdf')
    # st.write(pdf)

    if pdf is not None:
        # st.write(pdf.name)
        pdf_reader=PdfReader(pdf)
        # st.write(pdf_reader)
        
        text=""
        for page in pdf_reader.pages:
            text+=page.extract_text()
        # st.write(text)

        text_splitter= RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks=text_splitter.split_text(text=text)

        # st.write(chunks)

        #embeddings
        store_name=pdf.name[:-4]
        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl","rb") as f:
                VectorStore = pickle.load(f)
            # st.write("Embeddings Loaded from the Disk")
        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks,embedding=embeddings)
            with open(f"{store_name}.pkl","wb") as f:
                pickle.dump(VectorStore, f)
            # st.write("Embeddings Computation is Compeleted")
        
        #Accept user questions/query
        query = st.text_input("Ask questions about your PDF file:")
        # st.write(query)

        if query:
            docs = VectorStore.similarity_search(query=query, k=3)
            #context
            # st.write(docs)
            llm = OpenAI(model_name="gpt-4o")
            chain = load_qa_chain(llm=llm,chain_type="stuff")
            response=chain.run(input_documents=docs,question=query)
            st.write(response)

if __name__=='__main__':
    main()

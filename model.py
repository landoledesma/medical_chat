from langchain import PromptTemplate
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA,ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
import chainlit as cl

DB_FAISS_PATH = "vectorstore/db_faiss"

template_bot = """ 
            usa la siguiente pieza de informacion para responder la pregunta de usuario
            si no sabes la respuesta solo di : no tengo ese conocimiento,
            no trates de responderla
            Context:{}
            Question:{question}
            solo regresa la informacion relevante y nada mas 
"""
def custom_prompt():
    """
        Prompt template for QA retrival for each vector store
    """

    prompt = PromptTemplate(template=template_bot,input_variables=["context","question"])
    return prompt

def load_llm():
    llm  = ChatOpenAI(
        max_tokens=250,temperature=0.5
        )
    return llm

def retrival_qa_chain(llm,prompt,db):
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever = db.as_retriever(search_kwargs={'k':2}),
        return_source_documents = True,
        chain_type_kwargs = {'prompt':prompt}
    )
    return qa_chain

def qa_bot():
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(DB_FAISS_PATH,embeddings)
    llm = load_llm
    qa_prompt = retrival_qa_chain(llm,qa_prompt,db)

    return qa_bot

def final_result(query):
    qa_result = qa_bot
    response = qa_result({'query':query})
    return response
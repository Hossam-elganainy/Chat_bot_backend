from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain.agents import initialize_agent
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.mapreduce import MapReduceChain
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
import os

api_key = 'AIzaSyD4MUKPfo5cixAk1AvGLC7PmgUPYBG7WHg'
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = api_key

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("message/diabetes.pdf")
documents = loader.load()


from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(documents)


embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004", 
)

vector = FAISS.from_documents(documents, embeddings)


prompt = ChatPromptTemplate.from_template(
    """
    You are a conversational doctor experienced in diabetes.
    You must provide a response to the patient's question.
    Gender: Male.
    Age: 30 years old.
    
    in greeting, ask the patient how you can help them.
    Make your responses summarized, specific to the patient's question, easy to understand, and accurate.
    
    don't mention the patient's test results only if the patient asks about them.
    
    Answer all questions normally. If the question is related to medical tests or disease status, respond based on the context or general information. If the test results are not uploaded, do not delay the response or ask for the test first; just provide an answer based on the available information.
    in Medical Test Results, Eye Test Results the result is classified from another ai model and it's very accurate to rely on.
    If the question is specifically about the test results or disease status, and no tests have been uploaded, include this message at the end of your answer:
    "يجب رفع نتيجة الاختبار من صفحة الاختبارات \"http://127.0.0.1:5000/upload_test\""
    
    Answer in Arabic.

    Chat History:
    {history}
    
    Context:
    {context}

    Question:
    {input}

    Medical Test Result:
    {test_result}

    Eye Test Results:
    {eye_test_results}

    Please provide your response:
    """
)

documnt_chain = create_stuff_documents_chain(llm,prompt)
retriever = vector.as_retriever()
retriever_chain = create_retrieval_chain(retriever, documnt_chain)


def add_to_memory(memory,user_input, response):
    memory.save_context(user_input, response)
    return memory


def get_response(user_input,history,test_resutls=' ',eye_test_results=' '):
    # get history
    response = retriever_chain.invoke({
        "input": user_input,
        "test_result": test_resutls,
        "eye_test_results": eye_test_results,
        "history": history,
    }
    )
    return response['answer']


if __name__ == "__main__":
    pass
import os,time,sys
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader,UnstructuredPDFLoader,TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
# from langchain_community.embeddings import HuggingFaceInstructEmbeddings,HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from utils import load_pdf_file,load_text_file

# Dynamically add the root directory to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.append(project_root)

start=time.time()
load_dotenv()
from langchain_huggingface import HuggingFaceEmbeddings
# embeddings=HuggingFaceInstructEmbeddings(model_name='hkunlp/instructor-base')
embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-mpnet-base-v2')

artifacts_folder='Multiple_Source_Chat/artifacts'
faiss_index_path = os.path.join(artifacts_folder, "faiss_index")

# Ensure the artifacts folder exists
os.makedirs(artifacts_folder, exist_ok=True)

if os.path.exists(faiss_index_path):
    ## Load local vector store
    vector_store=FAISS.load_local(faiss_index_path,embeddings,allow_dangerous_deserialization=True)
else:
    vector_store=FAISS.from_documents(
                        embedding=embeddings,
                        documents=chunks
                        )
    ## Save vector store
    vector_store.save_local(faiss_index_path)
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

##Load Model
llm=ChatGroq(
    model='llama3-70b-8192',
    temperature=0,
    max_tokens=None,
    max_retries=2,
    timeout=10
)

## Load pdf and text file
Directory_path='Multiple_Source_Chat\data'
pdf_list=load_pdf_file(Directory=Directory_path)
txt_list=load_text_file(Directory=Directory_path)


## load pdf using loader and add in all docs
all_docs=[]
for filepath in pdf_list:
    loader=PyPDFLoader(filepath)
    docs=loader.load()
    all_docs.extend(docs)

## load text file and add in all docs
for file in txt_list:
    loader=TextLoader(file,encoding="utf-8")
    docs=loader.load()
    all_docs.extend(docs)


## Create chunks
splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks=splitter.split_documents(all_docs)

## Vector Store
# embeddings=HuggingFaceInstructEmbeddings(model_name='hkunlp/instructor-base')
embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-mpnet-base-v2')

artifacts_folder='Multiple_Source_Chat/artifacts'
faiss_index_path = os.path.join(artifacts_folder, "faiss_index")

# Ensure the artifacts folder exists
os.makedirs(artifacts_folder, exist_ok=True)

if os.path.exists(faiss_index_path):
    ## Load local vector store
    print("Loading from Exisiting Faiss Index")
    print('-'*140)
    vector_store=FAISS.load_local(faiss_index_path,embeddings,allow_dangerous_deserialization=True)
else:
    print("Creating New Faiss Index")
    print('-'*140)
    vector_store=FAISS.from_documents(
                        embedding=embeddings,
                        documents=chunks
                        )
    ## Save vector store
    vector_store.save_local(faiss_index_path)

## Retriever
retriever=vector_store.as_retriever()

memory=ConversationBufferMemory(memory_key='chat_history', return_messages=True)

## Conversation
conversation=ConversationalRetrievalChain.from_llm(
    llm=llm,
    memory=memory,
    retriever=retriever
)

while True:
    user_input=input("Ask Question (Enter quit or exit to exit) :")
    if user_input in ('quit','exit'):
        break
    result=conversation.invoke(user_input)
    print(result)


# print(f'Length of Chunks : {len(chunks)}')
# # print(pdf_list)
# print('-'*140)
print('-'*140)
print(f'Time Taken : {time.time()-start}')

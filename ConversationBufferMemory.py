from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from dotenv import load_dotenv

load_dotenv()
# os.environ['GROQ_API_KEY']=GROQ_API_KEY
prompt=PromptTemplate(
    template="This is my temp {folder}",
    input_variables=['folder']
)

# print(prompt.invoke({'folder':'sanga'}))

llm=ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

memory=ConversationBufferMemory()

conversation=ConversationChain(
    llm=llm,
    memory=memory,
    # verbose=True
)

while True:
    user_input=input("Enter the Question you want to ask:")
    if user_input in ['quit','exit']:
        break
    res=conversation.invoke(user_input)
    print(res['response'])
print('-'*150)
print(memory.buffer)
print('-'*150)
print(memory.load_memory_variables)
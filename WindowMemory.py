from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain

load_dotenv()

llm=ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

memory=ConversationBufferWindowMemory(k=1)

conversation=ConversationChain(
    llm=llm,
    memory=memory
)

while True:
    user_input=input("Enter the Question you want to ask:")
    if user_input in ['quit','exit']:
        break
    res=conversation.invoke(user_input)
    print(res['response'])
print('-'*140)
print(memory.buffer)
print('-'*140)
print(memory.load_memory_variables)
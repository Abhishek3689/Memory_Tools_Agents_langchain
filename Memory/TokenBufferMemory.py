from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.memory import ConversationTokenBufferMemory
from langchain_groq import ChatGroq

load_dotenv()

llm=ChatGroq(
    model='llama-3.1-8b-instant',
    temperature=0,
    max_tokens=None,
    max_retries=2,
    timeout=10
)

memory=ConversationTokenBufferMemory(llm=llm,max_token_limit=70)

conversation=ConversationChain(
    llm=llm,
    memory=memory,
    # verbose=True
)


while True:
    user_input=input("Ask:")
    if user_input in ['quit','exit']:
        break
    res=conversation.invoke(user_input)
    print(res['response'])
print('-'*140)
print(memory.buffer)
print('-'*140)
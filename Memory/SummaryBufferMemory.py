from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm=ChatGroq(
    model='llama-3.1-8b-instant',
    temperature=0,
    max_tokens=None,
    max_retries=2,
    timeout=10
)

memory=ConversationSummaryBufferMemory(llm=llm,max_token_limit=100)



story=llm.invoke("Tell me something about black hole")

text='''
A black hole is a region in space where the gravitational pull is so strong that nothing, including light, can escape. It is formed when a massive star collapses in on itself and its gravity becomes so strong that it warps the fabric of spacetime around it.

**Characteristics of Black Holes**

1. **Event Horizon**: The point of no return around a black hole is called the event horizon. Once something crosses the event horizon, it is trapped by the black hole's gravity and cannot escape.
2. **Singularity**: At the center of a black hole is a point called a singularity, where the density and gravity are infinite.
3. **Gravitational Pull**: Black holes have an incredibly strong gravitational pull, which is proportional to their mass.
4. **No Emission**: Black holes do not emit any radiation or light, making them invisible to us.
**Types of Black Holes**

1. **Stellar Black Holes**: Formed from the collapse of individual stars, these black holes are relatively small, with masses a few times that of the sun.
2. **Supermassive Black Holes**: Found at the centers of galaxies, these black holes have masses millions or even billions of times that of the sun.
3. **Intermediate-Mass Black Holes**: Black holes with masses that fall between those of stellar and supermassive black holes.
'''

memory.save_context({'input':'write a story'},{'output':f'{text}'})
# print('story :',text)
print('-'*130)
print(memory.buffer)
# print(type(story.content))
print('-'*130)
print(memory.load_memory_variables({}))
conversation=ConversationSummaryBufferMemory(llm=llm,memory=memory)
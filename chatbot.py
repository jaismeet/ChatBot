import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

load_dotenv()

# Verify API key is loaded into environment
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("Missing GOOGLE_API_KEY. Check your .env file.")

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  
    temperature=0.7,
)

# Initialize memory and chain structures
memory = ConversationBufferMemory()
chain = ConversationChain(llm=llm, memory=memory, verbose=False)

print("Chatbot (type 'quit' to exit)\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
        
    if not user_input:
        continue
        
    try:
        # Invoke the chain
        response = chain.invoke({"input": user_input})
        
        # Safely extract response text from the dictionary payload
        bot_output = response.get("response", "No response key found.")
        print(f"\nBot: {bot_output}\n")
    except Exception as e:
        print(f"\nAn error occurred: {e}\n")
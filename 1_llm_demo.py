from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",   
    google_api_key="Api_key"
)

print(llm.invoke("What is the capital of India?").content)













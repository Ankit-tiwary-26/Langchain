from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",   
    google_api_key="AIzaSyD5C-ebqeUv8OVsMmXtVkaSyOn79SgA7Ig"
)

print(llm.invoke("What is the capital of India?").content)













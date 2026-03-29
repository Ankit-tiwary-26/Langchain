from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7, max_output_tokens=2048)

result = model.invoke("What is the capital of India?")
print(result.content)
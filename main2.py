from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is conversation history {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="mango")
prompt =ChatPromptTemplate.from_template(template)
chain = prompt | model
def handle_converstion():
  context = ""
  while True:
    user_input = input(": ")
    if user_input == "exit":
      break

    r = chain.invoke({"context": context, "question": user_input})
    print(r)
    context+=f"\nUser: {user_input}\Ai:{r}"

handle_converstion()
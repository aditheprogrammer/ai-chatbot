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
context = ""
def handle_converstion(user_input):
  r = chain.invoke({"context": context, "question": user_input})
  return r

while True:
  user_input = input(": ")
  if user_input == "exit":
    break

  r=handle_converstion(user_input)
  context+=f"\nUser: {user_input}\Ai:{r}"
  print(r)
handle_converstion()
#some change to demo git
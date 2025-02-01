from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


class Chat:
  context = ""
  def __init__(self):
    self.question = ""
    self.model = ""
    self.prompt = ""
    model = OllamaLLM(model="mango")
    template = """
          Answer the question below.

          Here is conversation history {context}

          Question: {question}

          Answer:
          """
    prompt =ChatPromptTemplate.from_template(template)
    chain = prompt | model
    self.chain = chain
    
  def ans (self, user_input):
    r = self.chain.invoke({"context": Chat.context, "question": user_input})
    Chat.context+=f"\nUser: {user_input}\Ai:{r}"
    return (r)


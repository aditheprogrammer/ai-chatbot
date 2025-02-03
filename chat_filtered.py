import litellm
from guardrails import Guard
from guardrails.hub import ProfanityFree

class Chat:
  def __init__(self):
    self.guard = Guard().use(ProfanityFree())
    self.messages=[]
    
  def ans (self, user_input):
    self.messages.append({"role": "user", "content": user_input})
    try:
      validated_response = self.guard(
          litellm.completion,
          model="ollama/mango",
          max_tokens=2024,
          api_base="http://localhost:11434",
          messages=self.messages
      )
      bot_response = validated_response.validated_output
    except Exception as e:
      bot_response = "Sorry but I cant talk about that."
    self.messages.append({"role": "assistant", "content": bot_response})
    return (bot_response)


import litellm
import requests
from guardrails import Guard
from guardrails.hub import ProfanityFree
import json
from datetime import datetime, timedelta
from chat_filtered import Chatfiltered

class Chat:
  def __init__(self):
    self.guard = Guard().use(ProfanityFree())
    self.messages=[]
    
  def ans (self, user_input):

    self.messages.append({"role": "user", "content": user_input})

    bot_response = ""

    try:
      if not user_input.lower().startswith('medicine for'):
        raise Exception("Query not handled in medical context")
      disease = user_input[len("medicine for"):].strip()
      medical_api = "https://api.fda.gov/drug/event.json?search=patient.reaction.reactionmeddrapt:" + disease + "&limit=1"
      
      headers = {}
      payload = {}

      r = requests.request("GET", medical_api, headers=headers, data=payload)
      #print(r.text)
      if isinstance(r.text, str):  # If wd is a string, convert it to a dictionary
          r = json.loads(r.text)
      if 'error' in r:
        raise Exception("Query not handled in medical context")
      else:
        medicinal_product = (
            r.get('results', [{}])[0]
            .get('patient', {})
            .get('drug', [{}])[0]
            .get('medicinalproduct')
        )
        drug_dosage_text = (
            r.get('results', [{}])[0]
            .get('patient', {})
            .get('drug', [{}])[0]
            .get('drugdosagetext')
        )
        if(medicinal_product):
          bot_response = 'medicine: ' + medicinal_product
        if(drug_dosage_text):
          bot_response += ' dose: ' + drug_dosage_text
        if bot_response == "":
          raise Exception("Query not handled in medical context")
        bot_response = bot_response.lower()
    except Exception as e:
      cf = Chatfiltered()
      bot_response = cf.ans(user_input)
    self.messages.append({"role": "assistant", "content": bot_response})
    return (bot_response)


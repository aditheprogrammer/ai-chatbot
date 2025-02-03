import litellm
from guardrails import Guard
from guardrails.hub import ProfanityFree
from weather_chat import chatWeather
import json
from datetime import datetime, timedelta

class Chat:
  def __init__(self):
    self.guard = Guard().use(ProfanityFree())
    self.messages=[]
    
  def ans (self, user_input):

    self.messages.append({"role": "user", "content": user_input})
    
    if "weather" in user_input.lower():
      cw = chatWeather()
      wd = cw.ans()
      
      if isinstance(wd, str):  # If wd is a string, convert it to a dictionary
        wd = json.loads(wd)
      current_temp = wd["current"]["temperature_2m"]
      current_time = wd["current"]["time"]

      forecast = []
      i=0
      while(len(forecast)):  # Next 3 hours
        forecast_time = wd["hourly"]["time"][i]
        forecast_temp = wd["hourly"]["temperature_2m"][i]
        
        # Add the formatted forecast to the list
        if(forecast_time > current_time):
          forecast.append(f"At {forecast_time}, temperature: {forecast_temp}°C")
        i += 1
      # Construct the response
      bot_response = (
          f"The current temperature is {current_temp}°C.\n"
          f"Local time: {current_time}\n\n"
          f"Upcoming forecast:\n" + "\n".join(forecast)
      )

    else:
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


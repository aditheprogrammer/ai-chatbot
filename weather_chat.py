import requests


class chatWeather:
  def ans(query):
    url = "https://api.open-meteo.com/v1/forecast?latitude=27.736905977136452&longitude=85.3191974807736&current=temperature_2m&hourly=temperature_2m&timezone=Asia/Kathmandu"

    payload = {"latitude":27.736905977136452,"longitude":85.3191974807736}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return(response.text)

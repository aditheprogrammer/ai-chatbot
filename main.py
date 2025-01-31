import ollama

#Init
client = ollama.Client()

m = "mango"
while True:
  p = input("")
  if p == "quit":
    break
  else:
    response = client.generate(model=m,prompt=p)
    print(response.response)
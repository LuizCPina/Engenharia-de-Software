import requests
from rich import print

response = requests.get("https://api.github.com")
print(f"[green]Status Code do Github:[/green] {response.status_code}")


response = requests.get("https://www.youtube.com/")
print(f"[green]Status Code do Youtube:[/green] {response.status_code}")

response = requests.get("https://inatel.br/home/")
print(f"[green]Status Code do Inatel:[/green] {response.status_code}")

response = requests.get("https://httpbin.org/gety")
print(f"[green]Status Code de algo que nao existe:[/green] {response.status_code}")

response = requests.get("https://api.github.com/search/repositories",params =  "")
print(f"[green]Status Code de entidade nao processavel:[/green] {response.status_code}")

response = requests.get("https://chatgpt.com/")
print(f"[green]Status Code do ChatGPT:[/green] {response.status_code}")


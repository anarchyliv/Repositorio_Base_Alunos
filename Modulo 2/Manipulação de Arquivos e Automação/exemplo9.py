import requests
from bs4 import BeautifulSoup

# Passo 1:escolher URL
url = "https://sp.senai.br/unidade/santanadeparnaiba"

#Passso 2:Fazer a requisição do HTTP
resposta = requests.get(url)
if resposta.status_code == 200:
    #Passo 3:USar o Beautifulsoup para interpretar o HTML
    soup = BeautifulSoup(resposta.text,"html.parser")
    #Passo 4: Encontre o título da página
    titulo = soup.title.string
    #Passo 5:Imprimir o título
    #Print(f"O titulo da pagina e:{titulo}, o melhor do Brasil")
    print(f"O titulo da pagina e: {titulo}")
else:
    print("Erro nao acessar a pagina:",resposta.status_code)
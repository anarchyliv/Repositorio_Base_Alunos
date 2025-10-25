# 1° Instalamos o requests com o comando: pip install requests 
# 2° Importamos o requests para o nosso arquivo
import requests

res = requests.get("https://www.wikipedia.org")
print(res.status_code) # Verificar o status da requisição 
print(res.text[:500]) # Imprimir os prpimeiros 500 caracteres do conteúdo 
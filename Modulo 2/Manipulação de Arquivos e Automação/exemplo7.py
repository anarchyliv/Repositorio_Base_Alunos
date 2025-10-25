# Importamos a biblioteca 
import requests 
res = requests.get("https://www.globo.com/") # Criamos uma requisição requests 
try:
    resultado = res.raise_for_status() # Solicitamos o status da requisição 
    print(res) # Pedimos para imprimir o resultado
except Exception as exc:
    print("Há um problema: %s"% (exc)) # Indentificamos o erro



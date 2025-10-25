#lendo um arquivo do tipo Json
#Sempre inciamos com a impportção do json ou da biblioteca que utilizarmos
import json 
#Abriremos o arquivo e o modo "r" le esse arquivo
with open("dados.json","r",encoding="utf-8") as arquivo:
    dados = json.load(arquivo)#esse metodo json.loads converte o conteudo  do arquivo json em dicionario    
print(dados)
print(type(dados))
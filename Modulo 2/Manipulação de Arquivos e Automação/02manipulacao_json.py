#Criando um arquvo Json do zero
#Importar o json
import json

#Criar um dicionário Python

dados = {
    "nome":"Maria",
    "idade":30,
    "cursos":["python," "Machine Learning"]
}

#Criar um arquivo Json e escrever dentro dele

with open("dados.json","w",encoding="utf-8") as arquivo: # w é o modo para escrever, encoding é para ortografia utilizar os caracteres especiais
    json.dump(dados,arquivo,indent=4,ensure_ascii=False) # Json.dump converftte um dicio´nario em Json
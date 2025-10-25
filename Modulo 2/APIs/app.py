# No terminal:
# 1) Criamos um ambiente virtual com o comando:
# python -m venv .venv 
# 2) Ativamos o ambiente virtual com o comando:
# .\.ven\Scripts\activate
# 3) instalamos o flask com  o comando:
# pip install flask
# Caso o seu ambiente virtual não seja ativado é preciso pesquisar na 
# internet como liberar a execução
# dele no PowerShell e voltar a ativar o ambiente depois 

from flask import Flask, jsonify,make_response,request
from bd_livros import livros # aqui eu estou importando a lista de livros criado ( banco de dados)

#BIBLIOTECAS 
# jsonify = transfroma lista, dicionários etc em arquivos json. Só funciona com status code 200, ou seja
# quando a requisição é bem sucedida
# make_response = trsnaforma os json em metodos HTTP e permite que estilizemos nossa resposta
# e trata os erros
# requests = faz as requisições 

app = Flask(__name__) #instanciando o flask, ou seja, estou tornando o molde num objeto
app.config["JSON_SORT_KEYS"]= False

# GET - Listar todos os livros do nosso "banco de dados"
@app.route("/livros", methods=["GET"])
def get_livros():
    return make_response(jsonify(
        mensagem = "Lista de Livros Cadastrados",
        dados = livros
    ),200)

if __name__ == "__main__": # Esse comando permite que a api seja executada de maneira independente em outros arquivos 
    app.run(debug=True)
    
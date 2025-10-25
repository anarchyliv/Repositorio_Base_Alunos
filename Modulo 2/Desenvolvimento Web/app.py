# 1- instalar no terminal o flask com o comando:pip install flask
# 2- adiciconar as bibliotecas que usaremos no projeto
from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import json
import resend 

resend.api_key = "re_cdx9uzyx_Ca4CNnxQqRWW4p5WyMqAe6ik"  # chave da  API para envio de mensagem 

app = Flask(__name__)  # instaciamos a aplicação web
with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados= json.load(arquivo)

@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST":
        nome=request.form["name"]
        email=request.form["email"]
        mensagem=request.form["message"]

# montar o dicionário da nova mensagem 
        dados_mensagem = {
            "nome" :nome,
            "email" :email,
            "mensagem" :mensagem,
            "data" :f"{datetime.today()}"
        }
# adicionar e salvar o json:
        dados.append(dados_mensagem)
        with open("dados.json", "w",encoding="utf-8") as arquivo:
            json.dump(dados,arquivo, indent=4, ensure_ascii=False)
           
# envia email usando Resend
            r= resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to":"pereiraanalivia154@gmaill.com",
                "subject": f"Solicitação de Adoção {nome}",
                "html": f"<p>Email:{email}<br>{mensagem}</p>"
            })

# Após o POST - redireciona para enviar reenvio do fromulário
        return redirect(url_for("index.html"))
# GEt- renderizar a página
    return render_template("index.html")

if __name__ == "__main__":  # asseguramos a independencia do projeto
    app.run(debug=True)
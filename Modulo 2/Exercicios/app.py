from flask import Flask, request, url_for, render_template

app= Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    # Se a requisição for POST o usúario enviou o formulário
    if request.method == "POST":
        try:
            # 1.Capturar a opção e o número do formulário
            opcao= request.form
            num = float(request.form["num"])
            resultado = None

            # 2. Lógica de cálculo
            if opcao == "potenciacao":
                resultado = num ** 2
            elif opcao == "radiciacao":
                if num < 0:
                    erro = "Nãp é possivél calcular a raiz quadrada de um número negativo."  
                    return render_template("index.html", erro=erro)
                resultado = num ** 0.5
            return render_template("index.html", resultado =resultado, opcao_escolhida=opcao)      
        except ValueError:
            erro = "Por favor, digite apenas números válidos."
            return render_template("index.html", erro=erro)
    return render_template("index.html")    
if __name__ == "__main__":
    app.run(debug=True)

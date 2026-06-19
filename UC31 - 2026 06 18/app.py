from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)
app.secret_key = "abc123456"

votos = {
    "Opcao A": 0,
    "Opcao B": 0,
    "Opcao C": 0
}

@app.route("/")
def aaa():
    votou = request.cookies.get("votou")
    return render_template("index.html", votos=votos, votou=votou)

@app.route("/votar/<opcao>")
def votar(opcao):
    if request.cookies.get("votou"):
        return redirect("/resultado")

    votos[opcao] += 1

    resposta = make_response(redirect("/resultado"))
    resposta.set_cookie("votou", "sim")

    return resposta

@app.route("/resultado")
def resultado():
    total = sum(votos.values())

    return render_template(
        "registro.html",
        votos=votos,
        total=total
    )

if __name__ == "__main__":
    app.run(debug=True)

#All hail Shadow
from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def index():

    mensagem = ""

    if request.method == 'POST':
        nickname = request.form.get('nome')
        jogo = request.form.get('jogo')
        email = request.form.get('email')
        if not nickname or not jogo:
            mensagem = "Os campos são obrigatórios!."
        else:
            mensagem = f"Olá, seu nickname é {nickname}! Seu jogo escolhido foi {jogo} e seu email é {email}"

    return render_template('index.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)
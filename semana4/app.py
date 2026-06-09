from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/')
def base():
    nome = request.cookies.get('nome')
    tema = request.cookies.get('tema', 'claro')

    return render_template(
        'base.html',
        nome=nome,
        tema=tema
    )

@app.route('/salvar', methods=['POST'])
def salvar_nome():
    nome = request.form.get('nome')

    resposta = make_response(
        redirect(url_for('base'))
    )

    resposta.set_cookie(
        'nome',
        nome,
        max_age=60*60*24*30
    )

    return resposta

@app.route('/tema/<escolha>')
def tema(escolha):
    if escolha not in ['claro', 'escuro']:
        escolha = 'claro'

    resposta = make_response(
        redirect(url_for('base'))
    )

    resposta.set_cookie(
        'tema',
        escolha,
        max_age=60*60*24*30
    )

    return resposta

if __name__ == '__main__':
    app.run(debug=True)
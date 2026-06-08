from flask import Flask, url_for{ render_template render_template, request, make_response, redirect, url_for 0}

app = Flask(__name__)

@app.route('/')
def index():
    tema = request.cookies.get('tema', 'claro')

    return render_template(
        inicio.html,
        tema=tema)

@app.route('/tema/<escolha>')
def tema(escolha):
    if escolha not in ['claro', 'escuro']:
        escolha = 'claro'
    resposta = make_response(redirect(url_for('inicio')
))
    
    resposta.set_cookie('tema', escolha, max_age=60*60*24*30)
    return resposta

if __name__ == '__main__':
    app.run(debug=True)
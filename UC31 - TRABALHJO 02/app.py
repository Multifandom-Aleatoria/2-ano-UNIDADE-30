from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email', '').strip().lower()
    CPF = request.form.get('CPF', '').strip()
    
    if CPF and (len(CPF)) >=12:
        return "CPF inválido! O CPF deve conter exatamente 11 dígitos numéricos.", 400 

    if not nome or not email or not CPF:
        mensagem = "Os campos são obrigatórios!."
    else:
        mensagem = f"Olá, seu nome é {nome}! Seu email é {email} e seu CPF é {CPF}"
    return mensagem
if __name__ == '__main__':
    app.run(debug=True)
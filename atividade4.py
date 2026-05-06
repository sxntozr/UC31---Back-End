from flask import Flask, render_template

app = Flask(__name__)

# 1
@app.route('/ola/<nome>')
def nome(nome):
    return f'Olá, {nome}! Seja bem-vinda ao sistema.'

# 2
@app.route('/calculo/<int:n1>/<int:n2>')
def numero(n1, n2):
    resultado = n1 + n2
    return f'Resultado: {resultado}'

# 3
@app.route('/idade/<nome>/<int:idade>')
def dados(nome, idade):
    if idade >= 18:
        return f'{nome} é maior de idade.'
    else:
        return f'{nome} é menor de idade.'
    
# 4
@app.route('/produto/<nome>/<float:preco>')
def produto(produto, preço):
    return f'O/A {produto} custa R$ {preço}' 

# 5
@app.route('/repetir/<palavra>/<int:vezes>')
def repetir(palavra, vezes):
    return (palavra + '') * vezes

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def home():
    return 'OLLAALALAA'

@app.route('/pizzaria/<sabor>')
def tabela(sabor):
    if sabor == 'calabresa':
        return render_template('calabresa.html')
    elif sabor == 'margherita':
        return render_template('margherita.html')
    elif sabor == 'frango':
        return render_template('frango.html')
    else: 
       return 'Sabor não disponível'
    
if __name__ == '__main__':
    app.run(debug=True)
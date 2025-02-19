import json
from flask import Flask, render_template

app = Flask(__name__)

# Carregar os dados do JSON
def carregar_dados():
    with open("data.json", "r", encoding="utf-8") as file:
        return json.load(file)

@app.route('/')
def home():
    dados = carregar_dados()
    return render_template('index.html', sobre=dados["sobre"])

@app.route('/portfolio')
def portfolio():
    dados = carregar_dados()
    return render_template('portfolio.html', projetos=dados["projetos"])

@app.route('/contato')
def contato():
    dados = carregar_dados()
    return render_template('contato.html', sobre=dados["sobre"])

@app.route('/c')
def c():
    return "c"
@app.route('/d')
def d():
    return "d"

if __name__ == '__main__':
    app.run()

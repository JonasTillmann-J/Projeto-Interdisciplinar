# Projeto-Interdisciplinar
Projeto interdisciplinar do curso tecnico em desenvolvimento de sistemas cedup herman hering menistrados entre agosto a novenbro de 2024. gerido por Jonas tillmann Junior Programado por Jonas Tillmann Junior e Fabio Henrique laurentino, documentado por Igor Etur e layput Prototipado por Nicole Diel

# Tecnologias utilizadas
    -Python
    -Flask
    -SQL
    -HTML/CSS
    -JavaScript
    -Visual Studio Code
    -MySQL WorkBench
    -Git
# Logica de pastas e arquivos para o Flask
# Exemplo
      meu_projeto/
    │
    ├── app.py                        # Código Flask principal 
    ├── templates/                    # Pasta para arquivos HTML
    │       └──                       # Arquivos HTML principais
    │
    └── static/                       # Pasta para arquivos estáticos
            ├── css/
            │    └── style.css        # Arquivos CSS principais
            ├── js/
            │    └── script.js        # Arquivo JavaScript principal
            │
            └── images/               # Pasta para armazenar imagens
                    └── imagem.png    # Exemplo de imagem

# Implementação do Flask

Para a Programação de comunicação do servidor com a aplicação html preciso que seja feita uma função "def" para cara tela onde essa função terá os codigos para a ligação envio e recebimento de dados assim com a função "Render_Template para agilizar o processo e deixar mais estavel e com intuitividade do encapsulamento de cada dela exemplo abaixo

# Nosso Codigo Exemplo

from flask import Flask, request, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
    def cadastrar():
        if request.method == 'POST':
          # Código de conexão e inserção no banco de dados
           pass
     return render_template("cadastro.html")

# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
    def login():
      if request.method == 'POST':
            # Código de verificação de login
            pass
        return render_template("login.html")

# Rota para a página de perfil
@app.route('/perfil')
    def perfil():
        # Lógica para buscar dados do usuário
        return render_template("perfil.html")

if __name__ == '__main__':
    app.run(debug=True)
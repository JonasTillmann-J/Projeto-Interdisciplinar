# Projeto-Interdisciplinar
# Descrição Geral
Este é um projeto interdisciplinar do curso Técnico em Desenvolvimento de Sistemas do CEDUP Hermann Hering, realizado entre agosto e novembro de 2024. A equipe do projeto é composta por: Jonas Tillmann Junior (gestão e programação), Fabio Henrique Laurentino       (programação), Igor Etur (documentação) e Nicole Diel (prototipagem do layout).

# Linguagens Utilizadas.
-Python
-SQL
-HTML/CSS
-JavaScript
    
# Tecnologias Utilizadas.
-Flask
-Visual Studio Code
-MySQL WorkBench
-Git
    
# Logica de pastas e arquivos para o Flask
A estrutura de pastas do Flask foi projetada para organizar o código e recursos de forma eficiente, facilitando a manutenção e promovendo o trabalho colaborativo.

1. O arquivo principal app.py contém o código central, incluindo rotas e configurações.
2. A pasta templates organiza os arquivos HTML da interface do usuário, que são renderizados com o motor de templates Jinja, permitindo separação clara entre backend e frontend.
3. A pasta static armazena arquivos estáticos como CSS, JavaScript e imagens, essencial para estilização e interatividade.

# Exemplo de Estrutura de Pastas
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

# Implementação com Flask
O Flask foi escolhido pela sua simplicidade e eficiência como servidor para a aplicação. Ele permite uma estrutura modular e encapsulada que facilita a implementação de funcionalidades de inteligência artificial e segurança no envio e recebimento de dados.         Cada rota terá funções específicas para gerenciar as telas, garantindo estabilidade e segurança. Abaixo, um exemplo de implementação de rotas e renderização de templates:
    
Exemplo de Código com Flask com o nosso padrão

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

    Rota para a página de login
    @app.route('/login', methods=['GET', 'POST'])
        def login():
          if request.method == 'POST':
                # Código de verificação de login
                pass
            return render_template("login.html")

    Rota para a página de perfil
    @app.route('/perfil')
        def perfil():
            # Lógica para buscar dados do usuário
            return render_template("perfil.html")

    if __name__ == '__main__':
        app.run(debug=True)

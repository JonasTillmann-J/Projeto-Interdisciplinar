# Projeto-Interdisciplinar
# Descrição Geral
Este é um projeto interdisciplinar do curso Técnico em Desenvolvimento de Sistemas do CEDUP Hermann Hering, realizado entre agosto e novembro de 2024. A equipe do projeto é composta por: Jonas Tillmann Junior (gestão e programação), Fabio Henrique Laurentino (programação), Igor Etur(documentação) e Nicole Diel (prototipagem do layout).

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
1.  A estrutura de pastas do Flask foi projetada para organizar o código e recursos de forma eficiente, facilitando a manutenção e promovendo o trabalho colaborativo.

1.1 O arquivo principal app.py contém o código central, incluindo rotas e configurações.

1.2 A pasta templates organiza os arquivos HTML da interface do usuário, que são renderizados com o motor de templates Jinja, permitindo separação clara entre backend e frontend.

1.3 A pasta static armazena arquivos estáticos como CSS, JavaScript e imagens, essencial para estilização e interatividade.

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
1.  O Flask foi escolhido pela sua simplicidade e eficiência como servidor para a aplicação. Ele permite uma estrutura modular e encapsulada que facilita a implementação de funcionalidades de inteligência artificial e segurança no envio e recebimento de dados.         Cada rota terá funções específicas para gerenciar as telas, garantindo estabilidade e segurança. Abaixo, um exemplo de implementação de rotas e renderização de templates:
    
1.1 Exemplo de Código com Flask com o nosso padrão

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

# Responsividade das telas:

1.  Variáveis no arquivo raiz que podem ser utilizadas em qualquer lugar com a função var()
Geralmente, uso para manter um padrão nas medidas. Aqui não há muitos exemplos, mas, supondo que 
a --posicaoinput corresponda ao que é usado em uma tela de 1920p, em 1333p eu poderia apenas 
ajustar um valor para adequar corretamente. Deve haver uma medida mestre que, quando aplicada, 
modifica o elemento conforme cada tamanho de tela, funcionando apenas ao reduzir o valor base. 
No entanto, isso pode ser um pouco complicado de descobrir. 

2.  "@media(max-width: 1366px)" a produção principal desse site é feita em uma tela 1980p mas temos outros ambientes tambem que eu programo ele e pra isso que estou usando "@media(max-width: 1366px)" que será ativado quando um computador atender ao requisito de ter uma tela de 1366p. Isso refere-se à largurada tela, mas também pode ser ajustado informando a altura da tela.

2.  IMPORTANTE: INFORMAÇÕES ESSENCIAIS

2.1 Telas de 1366p seguem os atributos especificados aqui. Apenas os atributos listados sofrerão alterações; os demais obedecerão ao
padrão geral.

2.2 Às vezes, o "@media(max-width: 1366px)" acha que só pq é grande vale por um 1920p, mas não é o caso. Se algum atributo
não estiver respondendo ou mudando quando alterado neste arquivo, verifique no inspetor do navegador, na aba de estilos, se os
atributos listados aqui estão ativados (não riscados) ou não (riscados). Como "@media(max-width: 1366px)" está ao final do arquivo,
ele será exibido na mesma ordem no inspetor.

2.3  Escreva apenas o necessário. A "maldição" do CSS é que, quanto mais linhas, mais internamente problemático ele se torna; isso é
especialmente verdadeiro para "@media(max-width: 1366px)". Use os métodos `calc()` e `var()` conforme necessário e a vontade, mas
evite muitos "@media" para diferentes resoluções, pois isso pode complicar o código.

2.4  Para projetos futuros, "@media(max-width: 1366px)" pode ser útil ocasionalmente, mas, se o projeto se expandir, considere formas
mais robustas, como automatização com JavaScript ou frameworks especializados em responsividade. O Chrome permite ajustar o tamanho da
tela em pixels no inspetor, onde você pode experimentar a resolução 1366p em casa mesmo na tela 1920p, o @media, funcionaria no emulador
de telas.
from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector
import bcrypt
from mysql.connector import Error
import google.generativeai as genai

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.Hub.html')

# Rota para a página inicial/cadastro
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    connection = None
    cursor = None
    if request.method == 'POST':
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='12568709Fa!',
                database='Callista'
            )
            if connection.is_connected():
                cursor = connection.cursor()
                email_cadastro = request.form['iptEmailTcad']
                primeiro_nome = request.form['iptPnomeTcad']
                segundo_nome = request.form['iptSnomeTcad']
                primeira_senha = request.form['iptsenha1Tcad']
                segunda_senha = request.form['iptsenha2Tcad']


                # Criptografar a senha
                senha_hash = bcrypt.hashpw(primeira_senha.encode('utf-8'), bcrypt.gensalt())

                cursor.execute("SELECT Email FROM Cadastro WHERE Email=%s", (email_cadastro,))
                if cursor.fetchone():
                    return "Conta já existente com esse email."
                else:
                    cursor.execute(
                        "INSERT INTO Cadastro (PNomeCadastro, SNomeCadastro, PSenhaCadastro, Email) VALUES (%s, %s, %s, %s)",
                        (primeiro_nome, segundo_nome, senha_hash, email_cadastro)
                    )
                    connection.commit()
                    return render_template('index.chat.html')
            else:
                return "Conexão com o banco de dados falhou."

        except Error as e:
            return f"Erro ao conectar ao banco de dados: {e}"

        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()

    return render_template("index.cadrastro.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            # Inicialização da conexão e do cursor
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='12568709Fa!',
                database='Callista'
            )

            if connection.is_connected():
                cursor = connection.cursor()

                # Coleta de dados do formulário
                email_login = request.form.get('iptEmailLogin')
                senha_login = request.form.get('iptSenhaLogin')

                # Consulta ao banco de dados
                query = "SELECT Email, PSenhaCadastro FROM Cadastro WHERE Email = %s"
                cursor.execute(query, (email_login,))
                result = cursor.fetchone()

                if result and bcrypt.checkpw(senha_login.encode('utf-8'), result[1].encode('utf-8')):
                    return redirect(url_for('chat'))
                else:
                    return render_template('index.login.html', error="Credenciais inválidas. Tente novamente.")

            else:
                return "Conexão com o banco de dados falhou."

        except mysql.connector.Error as e:
            return f"Erro ao conectar ao banco de dados: {e}"

        finally:
            # Fecha o cursor e a conexão, se existirem
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()

    # Renderiza a página de login se for um GET ou falhar
    return render_template("index.login.html")

@app.route('/sobrenos')
def sobrenos():
    return render_template('index.sobrenos.html')

#----------------------------------------------------------------------- Chat -----------------------------------------------------------------------------

# Rota para a página de chat
@app.route('/chat')
def chat():
    return render_template("index.Chat.html")

# Rota de API para o chat
@app.route('/api/chat', methods=['POST'])
def IAgenerativa():
    # Extrai a mensagem do usuário do JSON recebido
    data = request.get_json()
    user_message = data.get('message')

    # Configura a chave da API da IA generativa
    genai.configure(api_key='AIzaSyBKrVKzkEiqrqTVraNwIv7ocebXVun3KGA')  # Substitua pela sua chave de API válida

    # Inicializa o modelo da IA
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Define o prompt com a mensagem do usuário
    prompt = f"Usuário disse: {user_message}"

    # Gera a resposta da IA com base no prompt
    try:
        response = model.generate_content(prompt)
        ia_response = response.text if response and response.text else "Desculpe, não consegui gerar uma resposta no momento."
    except Exception as e:
        ia_response = f"Erro ao gerar resposta: {e}"

    # Retorno da resposta da IA como JSON
    return jsonify({'response': ia_response})

if __name__ == '__main__':
    app.run(debug=True)

    #Criptografar senha

   

# Criptografando a senha
def criptografar_senha(senha):
    salt = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
    return senha_hash

# Verificando a senha
def verificar_senha(senha, senha_hash):
    return bcrypt.checkpw(senha.encode('utf-8'), senha_hash)

# Exemplo de uso
senha = "minhaSenhaSegura123!"
senha_hash = criptografar_senha(senha)
print(f"Senha criptografada: {senha_hash}")

# Verificação
senha_correta = verificar_senha("minhaSenhaSegura123!", senha_hash)
senha_errada = verificar_senha("senhaIncorreta", senha_hash)
print(f"Senha correta: {senha_correta}")
print(f"Senha errada: {senha_errada}")


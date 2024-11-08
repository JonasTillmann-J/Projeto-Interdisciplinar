from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error
import google.generativeai as genai

app = Flask(__name__)

# Rota para a página inicial/cadastro
@app.route('/', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='Callista'
            )

            if connection.is_connected():
                cursor = connection.cursor()
                email_cadastro = request.form['iptEmailTcad']
                cursor.execute("SELECT Email FROM Cadastro WHERE Email=%s", (email_cadastro,))
                if cursor.fetchone():
                    return "Conta já existente com esse email."
                else:
                    primeiro_nome = request.form['iptPnomeTcad']
                    segundo_nome = request.form['iptSnomeTcad']
                    primeira_senha = request.form['iptsenha1Tcad']
                    segunda_senha = request.form['iptsenha2Tcad']
                    cursor.execute(
                        "INSERT INTO Cadastro (PNomeCadastro, SNomeCadastro, PSenhaCadastro, SSenhaCadastro, Email) VALUES (%s, %s, %s, %s, %s)",
                        (primeiro_nome, segundo_nome, primeira_senha, segunda_senha, email_cadastro)
                    )
                    connection.commit()
                    return "Usuário cadastrado"
            else:
                return "Conexão com o banco de dados falhou."

        except Error as e:
            return f"Erro ao conectar ao banco de dados: {e}"

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    return render_template("index.cadrastro.html")

# Rota para a página de chat
@app.route('/chat')
def chat():
    return render_template("index.chat.html")

# Rota de API para o chat
@app.route('/api/chat', methods=['POST'])
def IAgenerativa():
    # Extrai a mensagem do usuário do JSON recebido
    data = request.get_json()
    user_message = data.get('message')

    # Configura a chave da API da IA generativa
    genai.configure(api_key='AIzaSyAt6SsBmKYMT5538fLdwkmGtUsCdYU4cRQ')  # Substitua pela sua chave de API válida

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

@app.route('/login')
def login():
    return render_template("index.login.html")

if __name__ == '__main__':
    app.run(debug=True)

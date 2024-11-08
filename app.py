from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error

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
    data = request.get_json()
    user_message = data.get('message')
    if not user_message:
        return jsonify({'error': 'Mensagem não fornecida'}), 400

    resposta = f"Você disse: {user_message}"
    return jsonify({'response': resposta})

@app.route('/login')
def login():
    return render_template("index.login.html")

if __name__ == '__main__':
    app.run(debug=True)

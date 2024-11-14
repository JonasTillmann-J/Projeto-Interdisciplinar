from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error
import google.generativeai as genai

app = Flask(__name__)

# Rota para a página inicial/cadastro
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    connection = None
    cursor = None
    if request.method == 'POST':
        usuario = 'root'
        senha = '12568709Fa!'
        database = 'Callista'
        host = 'localhost'

        try:
            connection = mysql.connector.connect(
                host=host,
                user=usuario,
                password=senha,
                database=database
            )
            #Verificação se ha Email Igual para realizar cadastro
            if connection.is_connected():
                cursor = connection.cursor()
                email_cadastro = request.form['iptEmailTcad']
                cursor.execute("SELECT Email FROM Cadastro WHERE Email=%s", (email_cadastro,))
                record = cursor.fetchone()

                if record:
                    return "Conta já existente com esse email."
                else:
                #Se não houver Email cadastrado sera cadastrado nessa condição
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
                return "Conexão Inválida"

        except Error as e:
            return f"Erro ao conectar ao banco de dados: {e}"

         #Apos todo o processo havera o fechamento da conexao do Banco de Dados
        finally:
            if  cursor:
                cursor.close
            if connection and connection.is_connected():
                connection.close

    return render_template("index.cadrastro.html")

@app.route('/', methods=['GET', 'POST'])
def login():
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
                email_login = request.form['iptEmailLogin']
                senha_login = request.form['iptSenhaLogin']
                cursor.execute("SELECT Email,Senha FROM Login WHERE Email AND Senha==%s", (email_login,senha_login))
                if cursor.fetchone():
                   email_login == 'iptEmailLogin' and senha_login == 'iptSenhaLogin'
                   render_template['index.Chat.html']
                else:
                 return print("Usuario Não Cadastrado")
            else:
                return "Conexão com o banco de dados falhou."

        except Error as e:
            return f"Erro ao conectar ao banco de dados: {e}"

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    return render_template("index.Chat.html")

#----------------------------------------------------------------------- Chat -----------------------------------------------------------------------------

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

if __name__ == '__main__':
    app.run(debug=True)

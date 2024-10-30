from flask import Flask, request, render_template
import mysql.connector
from mysql.connector import Error

#então fabio só pra vc entender tem uma area naquele README que te
#explica melhor oq vc vai ter que fazer pra manter a organização
#espero que entenda. <3 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        usuario = 'root'
        senha = ''
        database = 'Callista'
        host = 'localhost'

        try:
            connection = mysql.connector.connect(
                host=host,
                user=usuario,
                password=senha,
                database=database
            )

            if connection.is_connected():
                cursor = connection.cursor()
                email_cadastro = request.form['iptEmailTcad']
                cursor.execute("SELECT Email FROM Cadastro WHERE Email=%s", (email_cadastro,))
                record = cursor.fetchone()

                if record:
                    return "Conta já existente com esse email."
                else:
                    primeiro_nome = request.form['iptPnomeTcad']
                    segundo_nome = request.form['iptSnomeTcad']
                    primeira_senha = request.form['iptsenha1Tcad']
                    segunda_senha = request.form['iptsenha2Tcad']
                    sql_cadastrado = """
                    INSERT INTO Cadastro (PNomeCadastro, SNomeCadastro, PSenhaCadastro, SSenhaCadastro, Email)
                    VALUES (%s, %s, %s, %s, %s)
                    """
                    cursor.execute(sql_cadastrado, (primeiro_nome, segundo_nome, primeira_senha, segunda_senha, email_cadastro)) # type: ignore
                    connection.commit()
                    return "Usuário cadastrado"
            else:
                return "Conexão Inválida"

        except Error as e:
            return f"Erro ao conectar ao banco de dados: {e}"

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    return render_template("index.cadrastro.html")

if __name__ == '__main__':
    app.run(debug=True)
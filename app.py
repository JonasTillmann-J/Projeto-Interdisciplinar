import google.generativeai as genai
import time
import mysql.connector
from mysql.connector import Error
from flask import Flask, request, render_template 


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

    return render_template("index.cadrastro.html")  # Corrigido o nome do template para cadastro

# Rota para a página de chat
@app.route('/chat')
def chat():
    # Configuração da API
    genai.configure(api_key='AIzaSyAt6SsBmKYMT5538fLdwkmGtUsCdYU4cRQ')  # Substitua pela sua chave de API válida

    # Inicialização do modelo de geração
    model = genai.GenerativeModel('gemini-1.5-flash')

    def get_user_input(attempt=1):
        """Obtém informações do usuário sobre o contexto da ajuda necessária e adapta as perguntas se for a segunda tentativa."""
        print("Para fornecer a melhor ajuda, precisamos de algumas informações.")
    
        # Perguntas para a primeira tentativa
        if attempt == 1:
            area_conhecimento = input("Qual é a sua área de conhecimento (ex: Ciências Exatas, Humanas, Biológicas, etc.)? ")
            curso = input("Qual é o seu curso ou nível de formação (ex: Engenharia, Ensino Médio, MBA)? ")
            materia = input("Qual é a matéria ou disciplina específica? ")
            topico = input("Qual é o tópico ou pergunta específica para o qual você precisa de ajuda? ")
        else:
            # Perguntas para tentativas subsequentes, reformulando para obter mais clareza
            area_conhecimento = input("Vamos tentar de novo. Pode me dizer sua área de estudo principal (Exatas, Humanas, etc.)? ")
            curso = input("Em qual curso ou grau você está estudando? ")
            materia = input("Qual disciplina ou tema gostaria de explorar? ")
            topico = input("Especifique o tópico ou dúvida que você quer entender melhor: ")
        return area_conhecimento, curso, materia, topico

    def generate_academic_help(model, area_conhecimento, curso, materia, topico):
        """Gera conteúdo acadêmico com base nas informações fornecidas e trata erros de geração."""
        prompt = (
            f"Área de conhecimento: {area_conhecimento}\n"
            f"Curso/Nível: {curso}\n"
            f"Matéria: {materia}\n"
            f"Tópico: {topico}\n\n"
            "Forneça uma explicação clara e detalhada, incluindo exemplos práticos, se possível, "
            "para ajudar o estudante a entender o tópico."
        )
    
        try:
            # Geração do conteúdo
            response = model.generate_content(prompt)
            return response.text if response and response.text else None
        except Exception as e:
            print(f"Erro ao gerar resposta: {e}")
            return None

    def main():
        """Função principal para interagir com o estudante e gerar a resposta, repetindo as perguntas caso falhe."""
        attempt = 1
    
        while True:
            # Obtenção de informações do estudante
            area_conhecimento, curso, materia, topico = get_user_input(attempt)
        
            # Geração da resposta acadêmica
            resposta = generate_academic_help(model, area_conhecimento, curso, materia, topico)
        
            # Exibição da resposta ou aviso de falha
            if resposta:
                print("\nResposta Gerada:")
                print(resposta)
                break
            else:
                print("\nDesculpe, não consegui gerar uma resposta com as informações fornecidas. Vamos tentar novamente.")
                attempt += 1
                time.sleep(1)  # Pequeno atraso antes de repetir as perguntas para uma experiência mais natural

    # Execução do programa
    if __name__ == "__main__":
        main()
    return render_template("index.chat.html")  # Certifique-se de que o nome do arquivo está correto

if __name__ == '__main__':
    app.run(debug=True)
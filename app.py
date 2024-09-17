from flask import Flask, render_template
#importando as bibliotecas

app = Flask(__name__)
#Sla oq faz mas "n mexe Blz"

@app.route('/')

def index():
    return render_template('index1.html')
#função pra renderizar o index "não mexer"

if __name__ == '__main__':
    app.run(debug=True)
#tá dizendo que só vai funcionar se tiver algo pra ele renderizar "não mexer"
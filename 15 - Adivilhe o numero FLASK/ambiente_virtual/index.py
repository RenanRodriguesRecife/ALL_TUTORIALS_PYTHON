from flask import Flask
app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return 'Meu primeiro site'

@app.route('/sobre')
def sobre():
    return 'Sobre'


# Para compiliar
# Primeiro você deve exportar
# export FLASK_APP=index.py (Linux, Mac)
# set FLASK_APP=index.py (windows)
# flask run

#Para que todas a alteração seja atualizadas
#o modo debug mode deve está ativado
#export FLASK_ENV=development
#set FLASK_ENV_development (windows)
#flask run
# -*- coding: utf-8 -*-
from flask import Flask, redirect, render_template, url_for, request
import flask_login

# instancia o Flask
app = Flask(__name__)
# define a chave para criar o id de seção
app.secret_key = 'w34e'
# instancia o objeto que gerencia a seção de usuário
login_manager = flask_login.LoginManager()
# a partir daqui o LoginManager começa a monitorar as rotas da aplicação
login_manager.init_app(app)
# instancia a classe User


# gerenciamento de rotas do sistema
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():

    if request.method == 'GET':
        return render_template('cadastrar.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')


    return "Credenciais inválidas"


@app.route('/privado')
# decorator usado para rotas que exigem login
@flask_login.login_required
def privado():
    return render_template('admin.html')


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Area restrita do sistema'


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=8080, debug=False)
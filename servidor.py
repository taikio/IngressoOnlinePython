# -*- coding: utf-8 -*-
from flask import Flask, redirect, render_template, url_for, request, session, flash
from model import pessoa, ingresso
from dao import helper
from dao import connection, pessoaDao, ingressoDao, compraDao

app = Flask(__name__)
app.secret_key = 'jfhddnfvmg45g865fifhfFGCDFF'

_pessoa = pessoa.Pessoa()
_ingresso = ingresso.Ingresso()
_helper = helper.DaoHelper()
_helper.criarTabelas()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/cadastrar', methods=['GET','POST'])
def cadastrar():

    if request.method == 'GET':
        return render_template('cadastrar.html')

    nome = request.form['nome']
    email = request.form['email']
    username = request.form['username']
    senha = request.form['senha']

    if _pessoa.cadastrar(nome,email,username,senha):
        flash('Cadastro efetudado com sucesso')
        return redirect(url_for('logar'))

    flash('Nao foi possivel cadastrar o usuario')
    return redirect(url_for('home'))


@app.route('/logar', methods=['GET','POST'])
def logar():

    if request.method == 'GET':
        return render_template('login.html')

    username = request.form['username']
    senha = request.form['senha']

    if _pessoa.autenticar(username, senha):
        session['username'] = _pessoa.username
        session['senha'] = _pessoa.senha
        session['nivel_permissao'] = _pessoa.nivelPermissao

        return render_template('admin.html')

    return 'Usuário ou senha inválidos'

if __name__ == '__main__':
    app.run(port=8080, debug=True)


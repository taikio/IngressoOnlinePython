# -*- coding: utf-8 -*-
from flask import Flask, redirect, render_template, url_for, request, session, flash, g
from model import pessoa, ingresso
from dao import helper
from dao import connection, pessoaDao, ingressoDao, compraDao

app = Flask(__name__)
app.secret_key = 'jfhddnfvmg45g865fifhfFGCDFF'

_pessoa = pessoa.Pessoa()
_ingresso = ingresso.Ingresso()
_helper = helper.DaoHelper()
_helper.criarTabelas()
_listaDeIngressos = list()


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
        session['nivel_permissao'] = _pessoa.nivelPermissao

        print(session['nivel_permissao'])

        return redirect(url_for('loja'))

    return 'Usuário ou senha inválidos'


@app.route('/loja')
def loja():



    _listaDeIngressos = _ingresso.retornarTodos()
    if session:
        return render_template('loja.html')
    return redirect(url_for('logar'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/admin')
def admin():

    if session:
        if session['nivel_permissao'] == 'admin':
            return render_template('admin.html')

    return redirect(url_for('home'))

@app.route('/cadastraringresso', methods=['POST'])
def cadastrarIngresso():

    nome = request.form['nome']
    categoria = request.form['categoria']
    valor = request.form['valor']
    quantidade = request.form['quantidade']
    _ingresso.cadastrar(nome, categoria, valor, quantidade)

    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(port=8080, debug=True)


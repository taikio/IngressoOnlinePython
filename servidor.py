# -*- coding: utf-8 -*-
from flask import Flask, redirect, render_template, url_for, request, session, flash, g
from model import pessoa, ingresso, compra
from dao import helper
from dao import connection, pessoaDao, ingressoDao, compraDao

app = Flask(__name__)
app.secret_key = 'jfhddnfvmg45g865fifhfFGCDFF'

_pessoa = pessoa.Pessoa()
_ingresso = ingresso.Ingresso()
_compra = compra.Compra()
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
        if session:
            return redirect(url_for('home'))
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

    if session:
        return render_template('loja.html', lista=_ingresso.retornarTodos())
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


@app.route('/compraringresso', methods=['POST'])
def comprar():

    nome = request.form['nome']
    tipo = request.form['tipo']
    qtd = int(request.form['quantidade'])
    valorUnit = float(request.form['valor'])
    valorTotal = valorUnit * qtd
    comprador = session['username']

    print(nome +"-"+ tipo +"-"+ str(qtd) +"-"+ str(valorUnit) +"-"+ str(valorTotal)+"-"+ comprador)

    if _compra.cadastrar(nome,tipo,qtd,valorUnit,valorTotal,comprador):
        return redirect(url_for('loja'))

    return "404 - Não foi possível efetuar a compra, tente novamente mais tarde"


@app.route('/comprovante')
def retirarComprovante():

    lista = _compra.retornarPorUsuario(session['username'])
    return render_template('comprovante.html', lista=lista, user=session['username'])


if __name__ == '__main__':
    app.run(port=8080, debug=True)
    print("acesse com: localhost:8080")


#add/excluir/editar/mostrar todos/mostrar por id ou nome
from flask import Flask, jsonify, render_template, Blueprint, redirect, url_for,request
from flask_sqlalchemy import SQLAlchemy
from database import init_app, db
from DAO.campeoes import *
from repository.campeaoRepository import CampeaoRepository

campeoes_repository = CampeaoRepository()

campeoesController = Blueprint("campeao", __name__)
@campeoesController.route('/')
def index():
    return render_template("index.html")

@campeoesController.route('/ver-campeoes', methods=['GET'])
def ver_campeoes():
    print("controllert")
    campeoes = campeoes_repository.get_all_campeoes()
    print('indo pro rendertemplate')
    return render_template('get_all_campeao.html', campeoes=campeoes)

@campeoesController.route('/get_id/<int:id_campeao>', methods=['GET'])
def ver_id(id_campeao):
    campeao = campeoes_repository.get_campeao_by_id(id_campeao)
    return render_template("get_id_campeao.html", campeao=campeao)


@campeoesController.route('/add_campeao',methods=['POST', 'GET'])
def add_campeao():
    if request.method == 'POST':
        nome = request.form.get('nome')
        dificuldade = request.form.get('dificuldade')
        campeoes_repository.create_campeao(nome,dificuldade) #chama a função do repository que 
        return redirect(url_for('campeao.ver_campeoes'))
    return render_template('add_campeao.html')

    
@campeoesController.route('/update_campeao/<int:id_campeao>',methods=['POST','PUT', 'GET'])
def update_campeao(id_campeao):
    if request.method == 'PUT':
        nome = request.form.get('nome')
        dificuldade = request.form.get('dificuldade')
        campeoes_repository.update_campeao(id_campeao,nome,dificuldade) #chama a função do repository que 
        return redirect(url_for('campeao.update_campeoes'))
    return render_template('update_campeao.html')


@campeoesController.route('/delete_campeao',methods=['DELETE', 'GET'])
def delete_campeao(id_campeao):
    if request.method == 'DELETE':
        id_campeao = request.form.get('id_campeao')
        campeao = campeoes_repository.get_campeao_by_id(id)
        campeoes_repository.delete_campeao(campeao)
        return redirect(url_for('campeao.delete_campeoes'))
    return render_template('delete_campeao.html')
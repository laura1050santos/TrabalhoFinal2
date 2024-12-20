#add/excluir/editar/mostrar todos/mostrar por id ou nome
from flask import Flask, jsonify, render_template, Blueprint, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from database import init_db, db
from DAO import *
from repository import UserRepository

user_repository = UserRepository()

userController = Blueprint("User", __name__)

@userController.route('/ver-user')
def ver_user():
    user = user_repository.get_all_user()
    return render_template('lista_usuarios.html', user=user)

@userController.route('/add', methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        nome = request.form.get('register-nome')
        email = request.form.get('register-email')
        senha = request.form.get('register-senha')
        confirmar_senha = request.form.get('confirmar-senha')
        user_repository.create_user(nome, email, senha,confirmar_senha)
        
    return render_template('cadastro.html')

@userController.route('/users', methods=['GET'])
def get_users():
    users = user_repository.get_all_users()
    return jsonify([user.toJson() for user in users])

@userController.route('/user/<int:id_user>', methods=['PUT'])
def update_user(id_user):
    nome = request.get('name')
    email = request.get('email')
    updated_user = user_repository.update_user(id_user, nome, email)
    if updated_user:
        return jsonify({'id': updated_user.id, 'name': updated_user.name, 'email': updated_user.email})
    return jsonify({'error': 'User not found'}), 404

@userController.route('/user/<int:id_user>', methods=['DELETE'])
def delete_user(id_user):
    deleted_user = user_repository.delete_user(id_user)
    if deleted_user:
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'error': 'User not found'}), 404

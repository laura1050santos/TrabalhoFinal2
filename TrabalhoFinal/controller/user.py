from DAO import *
from repository import UserRepository
from flask import request, Blueprint, render_template
user_repository = UserRepository()

userController = Blueprint("user", __name__)

@userController.route('/')
def index():
    return render_template("index.html")

@userController.route('/add_user', methods=[ 'GET'])
def add_user():
    if request.method == 'GET':
        nome = request.form.get('register-nome')
        email = request.form.get('register-email')
        senha = request.form.get('register-senha')
        confirmar_senha = request.form.get('confirmar-senha')
        user_repository.create_user(nome, email, senha,confirmar_senha)
        return render_template('/user/cadastro_user.html' , mensagem="add feito com sucesso")
    print('indo pro return')
    return render_template('/user/cadastro_user.html' )


@userController.route('/ver-todos', methods=['GET'])
def get_users():
    users = user_repository.get_all_users()
    return render_template('/user/cadastro_user.html')


@userController.route('/user/update_user/', methods=['POST','GET'])
def update_user():
    id_user = request.get('id_user')
    nome = request.get('name')
    email = request.get('email')
    updated_user = user_repository.update_user(id_user, nome, email)
    if updated_user:
        return render_template('/user/get_all_user.html', mensagem= 'add com sucesso');
    return render_template('/user/update_user.html')

@userController.route('/delete_user', methods=['GET'])
def delete_user(id_user):
    deleted_user = user_repository.delete_user(id_user)
    if deleted_user:
        return render_template('/user/get_all_user.html')
    return render_template('/user/delete_user.html')

@userController.errorhandler(404) #erro de pagina não encontrada
def erro404(e):
    return render_template('404.html'), 404

@userController.errorhandler(401) #erro de pagina não autorizada
def erro404(e):
    return render_template('401.html'), 401

@userController.errorhandler(403) #acesso negado
def page_not_found(e):
    return render_template('403.html'), 403

@userController.errorhandler(500)  #erro interno no servidor
def page_not_found(e):
    return render_template('500.html'), 500
@userController.route('/ver-user')
def ver_user():
    user = user_repository.get_all_user()
    return render_template('/user/lista_usuarios.html', user=user)
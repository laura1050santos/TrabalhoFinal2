from DAO import UserDAO #importando a classe Dao
from flask import Flask, flash,session
class UserRepository:
    def __init__(self) -> None:
        self.userDAO = UserDAO()

    def get_all_user(self):
        return self.userDAO.get_all_user()#pega a função do DAO
    
    def get_user_by_id(self, id_user):
        if not id_user.isdigit():
            return self.userDAO.get_user(id_user)
        
    def get_user_by_email(self, email):
        return self.userDAO.get_user(email)

    def create_user(self, nome, email, senha,confirmar_senha):
        try:
            return self.userDAO.add_user(nome, email, senha)
        except Exception as e:
            return str(e)

    def update_user(self, id_user, nome, email, senha):
        return self.userDAO.update_user(id_user,nome, email, senha)

    def delete_user(self, id_user):
        return self.userDAO.delete_user(id_user)

    def login(self, email, senha):
        user = self.userDAO.get_user_email(email)
        if user:
            if user.senha == senha:
                session['user.id'] = user.id
                flash('Você está logado', 'success')
                return True
            else:
                flash('Senha inválida', 'error')
                return False
        else:
            flash('E-mail inválido', 'error') 
            return False

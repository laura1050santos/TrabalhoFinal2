from DAO import UserDAO #importando a classe Dao
from flask import Flask, flash,session
class UserRepository:
    def __init__(self) -> None:
        self.userDAO = UserDAO()

    def get_all_user(self):
        return self.userDAO.get_all_user()#pega a função do DAO
    
    def get_user_by_id(self, id_user):
        return self.userDAO.get_user(id_user)
    
    def get_user_by_email(self, email):
        return self.userDAO.get_user(email)

    def create_user(self, nome, email, senha,confirmar_senha):
        if len(nome) < 3:
            flash("a senha deve ter 3 caracteres", 'error') 
            return False
        if not email or '@' not in email:
            flash('E-mail inválido.', 'error')
            return False
        if len(senha) < 8 or len(senha) > 12 or not any(c.isdigit() for c in senha) or not any(c.isupper() for c in senha) or not any(c in '!@#$%^&*()' for c in senha):
            flash('Senha deve ter entre 8 e 12 caracteres, com pelo menos uma letra maiúscula, um número e um caractere especial.', 'error')
            return False
        if senha != confirmar_senha:
            flash('Senhas não coincidem.', 'error')
            return False
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
                flash('Você está logado', 'error')
            else:
                flash('Senha inválida', 'error')
        else:
            flash('E-mail inválido', 'error') 

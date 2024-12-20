from DAO.campeoes import CampeaoDAO #importando a classe Dao

class CampeaoRepository:
    def __init__(self) -> None:
        self.campeaoDAO = CampeaoDAO()

    def get_all_campeoes(self):
        print("passou pelo repository")

        return self.campeaoDAO.get_all_campeoes()#pega a função do DAO
    
    def get_campeao_by_id(self, id_campeao):
        return self.campeaoDAO.get_Campeao(id_campeao)

    def create_campeao(self, nome, dificuldade):
    #funcao, classe, regiao   
        return self.campeaoDAO.add_Campeao(nome, dificuldade  )  
        #funcao, classe, regiao   
    def update_campeao(self, id_campeao, nome, dificuldade):
        return self.campeaoDAO.update_Campeao(id_campeao, nome, dificuldade)
    #classe, funcao

    def delete_user(self, id_campeao):
        return self.campeaoDAO.delete_Campeao(id_campeao)
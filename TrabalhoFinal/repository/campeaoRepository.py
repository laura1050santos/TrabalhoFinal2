from DAO.campeoes import CampeaoDAO

class CampeaoRepository:
    def __init__(self) -> None:
        self.campeaoDAO = CampeaoDAO()

    def get_all_campeoes(self):
        campeoes = self.campeaoDAO.get_all_campeoes()
        if campeoes:
            mensagens = "Lista de campeões recuperada com sucesso."
            return True, mensagens, campeoes
        mensagens = "Nenhum campeão encontrado."
        return False, mensagen

    def get_campeao_by_id(self, id_campeao):
        if not id_campeao:
            mensagens = "ID do campeão é obrigatório."
            return False, mensagens
        campeao = self.campeaoDAO.get_Campeao(id_campeao)
        if campeao:
            mensagens = "Campeão encontrado com sucesso."
            return True, mensagens, campeao
        mensagens = "Campeão não encontrado."
        return False, mensagens

    def create_campeao(self, nome, dificuldade):
        if not nome or not dificuldade:
            mensagens = "Nome e dificuldade são obrigatórios."
            return False, mensagens
        if len(nome) < 3:
            mensagens = "O nome do campeão deve ter pelo menos 3 caracteres."
            return False, mensagens
        campeao_criado = self.campeaoDAO.add_Campeao(nome, dificuldade)
        if campeao_criado:
            mensagens = "Campeão criado com sucesso."
            return True, mensagens
        mensagens = "Erro ao criar o campeão."
        return False, mensagens

    def update_campeao(self, id_campeao, nome, dificuldade):
        if not id_campeao or not nome or not dificuldade:
            mensagens = "Todos os campos são obrigatórios."
            return False, mensagens
        if len(nome) < 3:
            mensagens = "O nome do campeão deve ter pelo menos 3 caracteres."
            return False, mensagens
        campeao_atualizado = self.campeaoDAO.update_Campeao(id_campeao, nome, dificuldade)
        if campeao_atualizado:
            mensagens = "Campeão atualizado com sucesso."
            return True, mensagens
        mensagens = "Erro ao atualizar o campeão."
        return False, mensagens

    def delete_campeao(self, id_campeao):
        if not id_campeao:
            mensagens = "ID do campeão é obrigatório."
            return False, mensagens
        campeao_deletado = self.campeaoDAO.delete_campeao(id_campeao)
        if campeao_deletado:
            mensagens = "Campeão deletado com sucesso."
            return True, mensagens
        mensagens = "Erro ao deletar o campeão."
        return False, mensagens
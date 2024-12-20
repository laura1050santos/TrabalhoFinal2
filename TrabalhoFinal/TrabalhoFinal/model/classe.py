from database import db
class Classe(db.Model):
    __tablename__ = 'classes'

    id_classe = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(255), nullable=True)

    id_funcao = db.Column(db.Integer, db.ForeignKey('funcoes.id_funcao'), nullable=False)
    campeoes = db.relationship('Campeao', back_populates='classe', lazy=True)
    itens = db.relationship('Item', back_populates='classe', lazy=True)
    funcao = db.relationship('Funcao', back_populates='classes', lazy=True)

    def __repr__(self):
        return f"<Classe {self.nome} - {self.desc}>"

    def toJson(self):
        return {
            'id_classe': self.id_classe,
            'nome': self.nome,
            'desc': self.desc,
            'id_funcao': self.id_funcao
        }
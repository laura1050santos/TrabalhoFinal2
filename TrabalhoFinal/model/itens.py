from database import db

class Item(db.Model):
    __tablename__ = 'itens'

    id_item = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(255), nullable=True)
    id_classe = db.Column(db.Integer, db.ForeignKey('classes.id_classe'), nullable=False)

    classe = db.relationship('Classe', back_populates='itens')
    
    def __repr__(self):
        return f"<Item {self.nome}>"

    def toJson(self):
        return {
            'id_item': self.id_item,
            'nome': self.nome,
            'desc': self.desc,
            'id_classe': self.id_classe
        }

from flask import Flask
from database import init_app
from controller.campeoes import campeoesController

app=Flask(__name__)

app.secret_key = 'Chave_mega_secreta' 

app.register_blueprint(campeoesController)

if __name__ == "__main__":
    init_app(app)
    app.run(debug=False)
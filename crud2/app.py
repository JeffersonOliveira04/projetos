from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Livros(db.Model):

    __tablename__= 'livraria'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    escritor = db.Column(db.String)

    def __init__(self, nome, escritor):
        self.nome = nome
        self.escritor = escritor


db.create_all()

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastro.html")

@app.route("/cadastro",methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        escritor = request.form.get("escritor") 

        if nome and escritor:
            l = Livros(nome, escritor)
            db.session.add(l)
            db.session.commit()

    return redirect(url_for("lista"))

@app.route("/lista")
def lista():
    livros = Livros.query.all()
    return render_template("lista.html", livros=livros)

@app.route("/excluir/<int:id>", methods=['GET'])
def excluir(id):
    livro = Livros.query.filter_by(id=id).first()

    db.session.delete(livro)
    db.session.commit()

    livros = Livros.query.all()
    return render_template("lista.html", livros=livros)

@app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
def atualizar(id):
    livros = Livros.query.filter_by(id=id).first()
    
    if request.method == "POST":
        nome = request.form.get("nome")
        escritor = request.form.get("escritor")   

        if nome and escritor:
            livros.nome = nome
            livros.escritor = escritor
            
            db.session.commit()
            
            return redirect(url_for("lista"))
    return render_template("/atualizar.html", livros=livros)



    if __name__== 'main':
        app.run(debug=True)
        
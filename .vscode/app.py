from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Livros(db.Model):

    __tablename__= 'livros'

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
            l = Livro (nome, escritor)
            db.session.add(l)
            db.session.commit()

    return redirect(url_for("index"))

@app.route("/lista")
def lista():
    livros = Livros.query.all()
    return render_template("lista.html", livros=Livros)

@app.route("/excluir/<int:id>")
def excluir(id):
    nome = nome.query.filter_by(_id=id).first()

    db.session.delete(nome)
    db.sessionc.commit()

    nome = Nome.query.all()
    #return render_template("lista.html" nome=nome)

@app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
def atualizar(id):
    nome = Nome.query.filter_by(_id=id).first()
    
    if request.method == "POST":
        nome = request.form.get("nome")
        escritor = request.form.get("escritor")   

        if nome and escritor:
            nome.nome = nome
            nome.escritor = escritor
            
            db.session.commit()
            
            return redirect(url_for("lista"))
    return render_template("/atualizar.html", nome=nome)



    if __name__== 'main':
        app.run(debug=True)
        
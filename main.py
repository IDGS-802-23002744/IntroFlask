from flask import Flask, render_template,request
from flask_wtf.csrf import CSRFProtect

import forms
import math

app = Flask(__name__)
app.secret_key="Clave secreta"
csrf=CSRFProtect()

@app.route('/')
def index():
    titulo="IDGS-802_Flask"
    lista=['Juan', 'Karla', 'Miguel', 'Ana']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route("/usuarios", methods=["GET", "POST"])

def usuarios():
    mat=0
    nom=''
    apa=''
    ama=''
    email=''
    usuarios_class=forms.UserForm(request.form)
    if request.method =='POST' and usuarios_class.validate():
        mat=usuarios_class.matricula.data
        nom=usuarios_class.nombre.data
        apa=usuarios_class.apaterno.data
        ama=usuarios_class.amaterno.data
        email=usuarios_class.correo.data

        message='Bienvenido{}'.format(nom)
        flash(message)
    
    return render_template("usuarios.html",form=usuarios_class
                            ,mat=mat,nom=nom,apa=apa,ama=ama,email=email
                            )


@app.route('/formularios')
def formularios():
    return render_template("formularios.html")


@app.route('/reportes')
def reportes():
    return render_template("reportes.html")
    

@app.route('/hola')
def hola():
    return "¡Hola, Hola!"

@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!"

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero, {}!".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {} nombre: {}".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    resultado = n1 + n2
    return f"<h1>Calculadora</h1><p>La suma de {n1} + {n2} es: <strong>{resultado}</strong></p>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func2(param="Juan"): 
    return f"<h1>Hola, {param}</h1>" 

@app.route("/operas")
def operas():
    return '''
    <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="paterno">Apellido Paterno:</label>
        <input type="text" id="paterno" name="paterno" required>
        
        <input type="submit" value="Enviar">
    </form>
    '''
    
@app.route("/operasBas", methods=["GET", "POST"])
def operas1():
    n1=0
    n2=0
    res=0
    if request.method == "POST":
        n1=request.form.get("n1")
        n2=request.form.get("n2")
        res=float(n1)/float(n2)
    return render_template("operasBas.html",n1=n1,n2=n2,res=res)

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    n1 = float(request.form.get("n1"))
    n2 = float(request.form.get("n2"))
    operacion = request.form.get("operacion")

    if operacion == "suma":
        res = n1 + n2
        texto = "La suma es"
    elif operacion == "resta":
        res = n1 - n2
        texto = "La resta es"
    elif operacion == "multiplicacion":
        res = n1 * n2
        texto = "La multiplicación es"
    elif operacion == "division":
        res = n1 / n2
        texto = "La división es"

    return f"{texto}: {res}"

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():

    return render_template("alumnos.html")

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    x1=0
    y1=0
    x2=0
    y2=0
    n1=0
    n2=0
    res=0

    if request.method == "POST":
            x1 = request.form.get("x1")
            y1 = request.form.get("y1")
            x2 = request.form.get("x2")
            y2 = request.form.get("y2")

            dx = float(x1) - float(x2)
            dy = float(y1) - float(y2)

            n1 = dx ** 2
            n2 = dy ** 2

            res = math.sqrt(n1 + n2)
    return render_template("distancia.html", res=res, x1=x1, y1=y1, x2=x2, y2=y2, n1=n1, n2=n2)

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)
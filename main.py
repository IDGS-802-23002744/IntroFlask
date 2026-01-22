from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    titulo="IDGS-802_Flask"
    lista=['Juan', 'Karla', 'Miguel', 'Ana']
    return render_template('index.html', titulo=titulo, lista=lista)

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
    
@app.route("/operasBas")
def operas1():
    return render_template("operasBas.html")

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

if __name__ == '__main__':
    app.run(debug=True)
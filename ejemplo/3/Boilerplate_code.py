#Importar el módulo Flask en el proyecto.
from flask import Flask, render_template
#Crear un objeto de la clase Flask.
app = Flask(__name__)

#La función route() de la clase Flask.
@app.route("/")

#‘/’ URL está vinculado con la función first_flask.
def student_webpage():
    # Crear una variable
    name = 'Jose Juan de las Rosas'
    # Pasar la variable en la pantalla.
    return render_template('index.html', student_name = name)

#Ejecutamos la app en el servidor local.
app.run(debug=True)

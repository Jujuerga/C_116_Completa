# Importar el módulo Flask en el el proyecto.
from flask import Flask

# Crear un ubjeto de la clase Flask.
app = Flask(__name__)

# La función route() de la clase Flask.
# '/' URL está vinculado con la función first flask.
@app.route("/")
def first_flask():
    return "Este en mi primer programa en Flask"

# Ejecutar la app en el servidor local.
#app.run()

# Definir una función con diferente punto final "/flask_2".
@app.route("/flask_2")
def second_flask():
    return "¡Python es divertido! ¡¡Programemos!!"

# Ejecutar usando un argumento depurativo (debug).
app.run(debug=True)

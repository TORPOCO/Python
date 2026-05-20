from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Definir una ruta
@app.route("/")
def hola_mundo():
    return "¡Hola Mundo con Flask!"

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)





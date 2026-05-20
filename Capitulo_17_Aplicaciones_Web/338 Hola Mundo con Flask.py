from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    app.logger.debug("Entramos al path de inicio")
    return '<h1>Hola Mundo</h1>'

if __name__ == '__main__':
    app.run(debug=True)
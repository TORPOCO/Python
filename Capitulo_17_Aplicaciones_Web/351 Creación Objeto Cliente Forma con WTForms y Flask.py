from flask import Flask, render_template
from S350_cliente_forma import ClienteForma
from cliente import Cliente
from cliente_dao import ClienteDAO

app = Flask(__name__)

app.config['SECRET_KEY'] = 'TORPOCO'
titulo_app ='Zona Fit (GYM)'

@app.route('/') #url: http://localhost:5000/
@app.route('/index.html') #url http://localhost:5000/index.html
def inicio():
    app.logger.debug("Entramos al path de inicio")

    #Recuperamos los clientes de bd
    clientes_db = ClienteDAO.seleccionar()
    #Creamos un objeto de cliente form vacio
    cliente = Cliente()
    #enviamos al contructor cliente los datos obtenidos de la clase ClienteForma
    cliente_forma = ClienteForma(obj=cliente)
    #return render_template("348 Botones Formulario con Bootstrap y Flask.html",titulo=titulo_app,clientes=clientes_db,forma=cliente_forma)
    #return render_template("348 Botones Formulario con Bootstrap y Flask.html",titulo=titulo_app,clientes=clientes_db,forma=cliente_forma)
    return render_template("353 Procesar Formulario con WTForms y Flask.html", titulo=titulo_app, clientes=clientes_db,
                           forma=cliente_forma)


if __name__ == '__main__':
    app.run(debug=True)
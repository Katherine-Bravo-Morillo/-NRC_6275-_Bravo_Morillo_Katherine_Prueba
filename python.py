#importamos la libreria Flask
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

#---------------------------------------
#Ruta que permite el acceso a la pagina principal
#---------------------------------------
@app.route('/')

#Funcion utilizada para hacer un llamado al index
def index():
    return render_template('index.html')

@app.route('/registro_Cuenta')

#Funcion para llamar al archivo de registro de cuenta
def registro_Cuenta():
    return render_template('/registro_Cuenta.html')

@app.route('/iniciar_Seccion')

#Funcion para llamar al archivo de inicio de seccion
def iniciar_Seccion():
    return render_template('/iniciar_Seccion.html')

#Funcion para llamar al archivo de registro Tienda

@app.route('/registro_Tienda')

#Funcion para llamar al archivo de inicio de seccion
def registro_Tienda():
    return render_template('/registro_Tienda.html')
#iniciamos la aplicacion
if __name__ == '__main__':
    app.run(debug=True)

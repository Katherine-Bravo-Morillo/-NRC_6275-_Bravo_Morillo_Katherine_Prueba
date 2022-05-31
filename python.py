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
#iniciamos la aplicacion
if __name__ == '__main__':
    app.run(debug=True)

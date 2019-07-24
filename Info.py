from flask import Flask
app = Flask(__name__)

@app.route ('/entero/<int:valor>')
def entero(valor):
    return "Esto es un digito %d " % valor


@app.route ('/flotante/<float:valor>')
def flotante(valor):
    return "Esto es un digito %f " % valor

if __name__ == '__main__':
    app.run (debug = True)


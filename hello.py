from flask import Flask
app = Flask(__name__)

#El @ es un decorador.
@app.route ('/')
def hello():
    return " Hello world in flask "

@app.route ('/dos')
def dos():
    return "se encuentra en dos "

if __name__ == '__main__':
    app.run(debug = True)

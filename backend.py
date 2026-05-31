from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Usuario de prueba
USUARIO = "admin"
PASSWORD = "1234"

# Productos de prueba
productos = {
    "P001": {
        "nombre": "Laptop Lenovo",
        "precio": 2500
    },
    "P002": {
        "nombre": "Mouse Logitech",
        "precio": 80
    },
    "P003": {
        "nombre": "Teclado Mecanico",
        "precio": 150
    }
}

# LOGIN
@app.route('/')
def login():
    return render_template('login.html')


# VALIDAR USUARIO
@app.route('/validar', methods=['POST'])
def validar():

    usuario = request.form['usuario']
    password = request.form['password']

    if usuario == USUARIO and password == PASSWORD:
        return redirect('/principal')

    return redirect('/')


# VENTANA PRINCIPAL
@app.route('/principal')
def principal():
    return render_template('principal.html')


# BUSCADOR
@app.route('/buscar')
def buscar():
    return render_template('buscador.html')


# BUSCAR PRODUCTO
@app.route('/buscar_producto', methods=['POST'])
def buscar_producto():

    codigo = request.form['codigo']

    producto = productos.get(codigo)

    return render_template(
        'buscador.html',
        producto=producto
    )


# SALIR
@app.route('/salir')
def salir():
    return redirect('/')


import os

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000))
    )
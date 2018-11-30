#!/usr/bin/env python
import csv
import funciones
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
# from flask_moment import Moment
from flask_script import Manager
from forms import LoginForm, SaludarForm, RegistrarForm, ProductForm, ClientForm

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
# moment = Moment(app)

app.config['SECRET_KEY'] = 'un string que funcione como llave'


@app.route('/')
def index():
    return render_template('index.html', fecha_actual=datetime.utcnow())


@app.route('/saludar', methods=['GET', 'POST'])
def saludar():
    formulario = SaludarForm()
    if formulario.validate_on_submit():
        print(formulario.usuario.name)
        return redirect(url_for('saludar_persona', usuario=formulario.usuario.data))
    return render_template('saludar.html', form=formulario)


@app.route('/saludar/<usuario>')
def saludar_persona(usuario):
    return render_template('usuarios.html', nombre=usuario)


@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_interno(e):
    return render_template('500.html'), 500


@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        with open('usuarios') as archivo:
            archivo_csv = csv.reader(archivo)
            registro = next(archivo_csv)
            while registro:
                if formulario.usuario.data == registro[0] and formulario.password.data == registro[1]:
                    flash('Bienvenido')
                    session['username'] = formulario.usuario.data
                    return render_template('ingresado.html')
                registro = next(archivo_csv, None)
            else:
                flash('Revisá nombre de usuario y contraseña')
                return redirect(url_for('ingresar'))
    return render_template('login.html', formulario=formulario)


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    formulario = RegistrarForm()
    if formulario.validate_on_submit():
        if formulario.password.data == formulario.password_check.data:
            with open('usuarios', 'a+') as archivo:
                archivo_csv = csv.writer(archivo)
                registro = [formulario.usuario.data, formulario.password.data]
                archivo_csv.writerow(registro)
            flash('Usuario creado correctamente')
            return redirect(url_for('ingresar'))
        else:
            flash('Las passwords no matchean')
    return render_template('registrar.html', form=formulario)


@app.route('/secret', methods=['GET'])
def secreto():
    if 'username' in session:
        return render_template('private.html', username=session['username'])
    else:
        return render_template('sin_permiso.html')


@app.route('/logout', methods=['GET'])
def logout():
    if 'username' in session:
        session.pop('username')
        return render_template('logged_out.html')
    else:
        return redirect(url_for('index'))

@app.route('/lista')
def lista():
    return render_template('lista.html', tabla = funciones.salesData())

#PRODUCTOS POR CLIENTE
@app.route('/productosporcliente', methods=['GET', 'POST'])
def formBusquedaCliente():
    form = ClientForm()
    saleData = funciones.salesData()

    if form.validate_on_submit():
        data = form.client.data
        client = data.title()

        clientList = funciones.consultedDataClient(client, saleData)  
        return render_template('consultas/productos-por-cliente-form.html', form=form, searchClient=client, lista=clientList)
        
        if len(clientList) == 0:
            clientList = None
        else:
            return redirect(url_for('tableProductsPerClient', client=client))
    
    return render_template('consultas/productos-por-cliente-form.html', form=form)

@app.route('/productosporcliente/<client>')
def tableProductsPerClient(client):
    saleData = funciones.salesData()
    completeTable = funciones.completeTable(client, saleData)
    return render_template('consultas/productos-por-cliente-tabla.html', cliente=client.title(), tabla=completeTable)

#CLIENTES POR PRODUCTO
@app.route('/clientesporproducto', methods=['GET', 'POST'])
def formBusquedaProducto():
    form = ProductForm()
    saleData = funciones.salesData()

    if form.validate_on_submit():
        data = form.product.data
        product = data.title()

        productList = funciones.consultedDataProduct(product, saleData)  
        return render_template('consultas/clientes-por-producto-form.html', form=form, searchProd=product, lista=productList)
        
        if len(productList) == 0:
            productList = None
        else:
            return redirect(url_for('tableClientPerProduct', product=product))
    
    return render_template('consultas/clientes-por-producto-form.html', form=form)

@app.route('/clientesporproducto/<product>')
def tableClientPerProduct(product):
    saleData = funciones.salesData()
    completeTable = funciones.completeTable(product, saleData)
    return render_template('consultas/clientes-por-producto-tabla.html', product=product.title(), tabla=completeTable)

@app.route('/masvendidos')
def productosMasVendidos():
    saleData = funciones.salesData()
    try:
        plusProducts = funciones.productosMasVendidos(saleData)
        tableComplete = funciones.ordenarTablaDescendente(plusProducts, 'PRODUCTO', 'CANTIDAD')
    except:
        return render_template('consultas/productos-mas-vendidos.html', table=saleData)
    return render_template('consultas/productos-mas-vendidos.html', table=tableComplete)

@app.route('/masgastaron')
def clientesMasGastaron():
    saleData = funciones.salesData()
    try:  
        plusClients = funciones.clientesQueMasCompraron(saleData)
        tableComplete = funciones.ordenarTablaDescendente(plusClients, 'CLIENTE', 'PRECIO')
    except:
        return render_template('consultas/clientes-mas-gastaron.html', table=saleData)
    return render_template('consultas/clientes-mas-gastaron.html', table=tableComplete)

if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    manager.run()

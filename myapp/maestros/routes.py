from flask import Blueprint, render_template, request, redirect, url_for
from main import consultarMaestros, insertarMaestro, modificarMaestro, buscarMaestro, eliminarMaestro

maestros = Blueprint('maestros', __name__)

@maestros.route('/getMaestros', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        maestros = consultarMaestros()
        return render_template('maestros.html', maestros=maestros)
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correoElectronico = request.form['correoElectronico']
        insertarMaestro(nombre, apellido, correoElectronico)
        return redirect(url_for('maestros.index'))
    

@maestros.route('/editar', methods=['GET', 'POST'])
def editar():
    if request.method == 'GET':
        id = request.args.get('id')
        nombre = request.args.get('nombre')
        apellido = request.args.get('apellido')
        correoElectronico = request.args.get('correoElectronico')
        return render_template('modificarMaestro.html', id=id, nombre=nombre, apellido=apellido, correoElectronico=correoElectronico)
    
    if request.method == 'POST':
        id = request.form['idMaestroED']
        nombre = request.form['nombreED']
        apellido = request.form['apellidoED']
        correoElectronico = request.form['correoElectronicoED']
        modificarMaestro(id,nombre, apellido, correoElectronico)
        return redirect(url_for('maestros.index'))
    

@maestros.route('/buscarMaestro', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        nombreMaestro = request.form['bsqMaestro']
        filtro = buscarMaestro(nombreMaestro)
        return render_template('buscarMaestro.html', filtro=filtro)
    

@maestros.route('/eliminar')
def eliminar():
        id = request.args.get('id')
        eliminarMaestro(id)
        return redirect(url_for('maestros.index'))
  




    


    


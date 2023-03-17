from flask import Blueprint, render_template, request, redirect, url_for
from main import consultarAlumno, insertarAlumno, modificarAlumno, buscarAlumno, eliminarAlumno

alumnos = Blueprint('alumnos', __name__)

@alumnos.route('/getAlumnos', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        alumnos = consultarAlumno()
        return render_template('alumnos.html', alumnos=alumnos)
    
    if request.method == 'POST':
        nombreAlum = request.form['nombreAlum']
        apellidoAlum = request.form['apellidoAlum']
        correoElecAlum = request.form['correoElecAlum']
        insertarAlumno(nombreAlum, apellidoAlum, correoElecAlum)
        return redirect(url_for('alumnos.index'))
    
@alumnos.route('/editarAlumno', methods=['GET', 'POST'])
def editarAlumno():
    if request.method == 'GET':
        idAlumno = request.args.get('idAlumno')
        nombreAlum = request.args.get('nombreAlum')
        apellidoAlum = request.args.get('apellidoAlum')
        correoElecAlum = request.args.get('correoElecAlum')
        return render_template('modificarAlumno.html', idAlumno=idAlumno, nombreAlum=nombreAlum, apellidoAlum=apellidoAlum, correoElecAlum=correoElecAlum)
    

    if request.method == 'POST':
        idAlumno = request.form['idAlumnoED']
        nombreAlum = request.form['nombreAlumED']
        apellidoAlum = request.form['apellidoAlumED']
        correoElecAlum = request.form['correoElecAlumED']
        modificarAlumno(idAlumno,nombreAlum, apellidoAlum, correoElecAlum)
        return redirect(url_for('alumnos.index'))
        

@alumnos.route('/buscarAlumno', methods=['GET', 'POST'])
def buscarAlumno():
    nombreAlum = request.args.get('nombreAlum')
    filtro = buscarAlumno(nombreAlum)
    return render_template('alumnos.html', alumnos=filtro)

@alumnos.route('/eliminarAlumno')
def deleteAlumno():
    idAlumno = request.args.get('idAlumno')
    eliminarAlumno(idAlumno)
    return redirect(url_for('alumnos.index'))


    


    

    

   





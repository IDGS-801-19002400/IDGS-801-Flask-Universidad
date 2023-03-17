from db import connection

#metodo que compruebe la conexion a la base de datos
def verificarConexion():
    try:
        conexion = connection()
        conexion.commit()
        print("Conexion exitosa")
        conexion.close()
        return True
    except:
        print("Conexion fallida")
        return False
    
#metodo que muestra los datos de la tabla maestros
def consultarMaestros():
     try:
         
         conn = connection()
         with conn.cursor() as cursor:
            cursor.execute('CALL consultar_maestros()')
            maestros = cursor.fetchall()
            return maestros
       
     except Exception as e:
         print("Error al consultar los maestros: ", e)

#metodo que inserta un nuevo maestro
def insertarMaestro(nombre, apellido, correoElectronico):
    try:
        conn = connection()
        with conn.cursor() as cursor:
            cursor.execute('CALL insertar_maestro(%s, %s, %s )', (nombre, apellido, correoElectronico))
            conn.commit()
    except Exception as e:
        print("Error al insertar el maestro: ", e)


#metodo que modifica un maestro
def modificarMaestro(idMaestro, nombre, apellido, correoElectronico):
    try:
        conn = connection()
        with conn.cursor() as cursor:
            cursor.execute('CALL modificar_maestro(%s, %s, %s, %s )', ( idMaestro,nombre, apellido, correoElectronico))
            conn.commit()
    except Exception as e:
        print("Error al modificar el maestro: ", e)


#metodo que busca un maestro
def buscarMaestro(nombreMaestro):
     try:
        conn = connection()
        with conn.cursor() as cursor:
            cursor.execute('CALL buscar_maestro(%s)', (nombreMaestro))
            maestro = cursor.fetchall()
            return maestro
     except Exception as e:
            print("Error al buscar el maestro: ", e)

#metodo que elimina un maestro
def eliminarMaestro(idMaestro):
    try:
        conn = connection()
        with conn.cursor() as cursor:
            cursor.execute('CALL eliminar_maestro(%s)', (idMaestro))
            conn.commit()
    except Exception as e:
        print("Error al eliminar el maestro: ", e)

#metodo que consulta los alumnos
def consultarAlumno():
        try:
            conn = connection()
            with conn.cursor() as cursor:
                cursor.execute('CALL consultar_alumno()')
                alumnos = cursor.fetchall()
                return alumnos
        
        except Exception as e:
            print("Error al consultar los alumnos: ", e)


#metodo que inserta un nuevo alumno
def insertarAlumno(nombreAlumno, apellidoAlumno, correoElecAlumno):
    try:
        conn = connection()
        with conn.cursor() as cursor:
            cursor.execute('CALL insertar_alumno(%s, %s, %s )', (nombreAlumno, apellidoAlumno, correoElecAlumno))
            conn.commit()
    except Exception as e:
        print("Error al insertar el alumno: ", e)


#metodo que modifica un alumno
def modificarAlumno(idAlumno, nombreAlumno, apellidoAlumno, correoElecAlumno):
    try:
        conn = connection()
        with conn.cursor() as cursor:
            cursor.execute('CALL modificar_alumno(%s, %s, %s, %s )', ( idAlumno,nombreAlumno, apellidoAlumno, correoElecAlumno))
            conn.commit()
    except Exception as e:
        print("Error al modificar el alumno: ", e)

#metodo que busca un alumno
def buscarAlumno(nombreAlumno):
        try:
            conn = connection()
            with conn.cursor() as cursor:
                cursor.execute('CALL buscar_alumno(%s)', (nombreAlumno))
                alumno = cursor.fetchall()
                return alumno
        except Exception as e:
                print("Error al buscar el alumno: ", e)

#metodo que elimina un alumno
def eliminarAlumno(idAlumno):
    try:
        conn = connection()
        with conn.cursor() as cursor:
            cursor.execute('CALL eliminar_alumno(%s)', (idAlumno))
            conn.commit()
    except Exception as e:
        print("Error al eliminar el alumno: ", e)




         



    
    

        

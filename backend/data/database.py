import backend.clases.usuario
import backend.clases.diagnostico
import backend.clases.resumen
import pymysql   # Importamos biblioteca pymysql que nos permitira el manejo de bases de datos MySQL en Python


'''
se realiza la conexion con la funcion .connect() en donde nos pedira los datos del host, usuario, contraseña y la base de datos

'''


# Conector entre el programa y la base de datos
def conectar():
    conexion = pymysql.connect( 
        host="localhost",
        user="vscode_user",
        password="user123",
        database="PI_DB",
        cursorclass = pymysql.cursors.DictCursor 
        )
    return conexion


conexion = conectar()

# Funciones correspondiente a las consultas de las tablas
# 1
def show_usuarios(conexion):

    with conexion.cursor() as cursor:

        cursor.execute("SELECT * FROM usuario;")
        usuarios = cursor.fetchall()
        
        '''for usuario in usuarios:
            print('Usuario:',usuario[0],'\nNombre:',usuario[2])
            print('\n')'''

        return usuarios
#1.1

def show_usuario(conexion, id_usuario,u_password):

    with conexion.cursor() as cursor:

        query = "SELECT * FROM usuario WHERE id_usuario = %s AND  u_password  = %s "
        cursor.execute(query, (id_usuario,
                               u_password))
        usuario = cursor.fetchone()

        return usuario
#1.2

def show_usuarioQR(conexion,qr_acceso):

    with conexion.cursor() as cursor:
        query = "SELECT * FROM usuario WHERE QR_acceso = %s"
        cursor.execute(query,qr_acceso)
        usuario = cursor.fetchone()

        return usuario


def insertar_usuario(conexion,usuario):

    with conexion.cursor() as cursor:

        query = """INSERT INTO usuario
                 (id_usuario,
                 u_password,
                 nombre,
                 fecha_nacimiento,
                 tipo_u,
                 tipo_sangre,
                 d_especialidad,
                 QR_acceso,
                 correo_electronico,
                 telefono,
                 pad_Cronico,
                 donador_organos,
                 accede_transfucion) 
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query,(  usuario.id_usuario,
                                usuario.u_password,
                                usuario.nombre,
                                usuario.fecha_nacimiento,
                                usuario.tipo_u,
                                usuario.tipo_sangre,
                                usuario.d_especialidad,
                                usuario.qr_acceso,
                                usuario.correo_electronico,
                                usuario.telefono,
                                usuario.pad_cronico,
                                usuario.donador_organos,
                                usuario.accede_transfucion))
        conexion.commit()

        
        return{
                "id_usuario": usuario.id_usuario,
                "u_password": usuario.u_password,
                "nombre":usuario.nombre,
                "fecha_nacimiento":usuario.fecha_nacimiento,
                "tipo_u":usuario.tipo_u,
                "tipo_sangre": usuario.tipo_sangre,
                "d_especialidad":usuario.d_especialidad,
                "qr_acceso": usuario.qr_acceso,
                "correo_electronico": usuario.correo_electronico,
                "telefono": usuario.telefono,
                "pad_cronico": usuario.pad_cronico,
                "donador_organos": usuario.donador_organos,
                "accede_transfucion": usuario.accede_transfucion
                }
# 2
def show_diagnosticos(conexion,id_usuario):

    with conexion.cursor() as cursor:
        query = """
                        SELECT d.*, u.nombre AS nombre_paciente, m.nombre AS nombre_medico
                        FROM diagnostico d
                        LEFT JOIN usuario u ON d.id_paciente = u.id_usuario
                        LEFT JOIN usuario m ON d.id_usuario = m.id_usuario
                        WHERE d.id_usuario = %s OR d.id_paciente = %s
                        ORDER BY d.fecha DESC
                """
        cursor.execute(query, (id_usuario,id_usuario))
        diagnosticos = cursor.fetchall()
        

        return diagnosticos
# 2.1
def insertar_diagnostico(conexion,diagnostico):

    with conexion.cursor() as cursor:

        query = "INSERT INTO diagnostico(id_usuario,id_paciente,d_especialidad,fecha,diagnostico)VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(query,(diagnostico.id_usuario,
                              diagnostico.id_paciente,
                              diagnostico.d_especialidad,
                              diagnostico.fecha,
                              diagnostico.diagIN))

        conexion.commit()

        return {
                "id_usuario":diagnostico.id_usuario, 
                "id_paciente":diagnostico.id_paciente, 
                "fecha":diagnostico.fecha,
                "diagnostico": diagnostico.diagIN
                }

def insertar_resumen(conexion,resumen):
    
    with conexion.cursor() as cursor:
        query = "INSERT INTO resumen(id_usuario,fecha,resumen) VALUES(%s,%s,%s)"
        cursor.execute(query,(resumen.id_usuario,
                              resumen.fecha,
                              resumen.summary))
        conexion.commit()

        return{
                "id_usuario":resumen.id_usuario,
                "fecha":resumen.fecha,
                "resumen":resumen.summary
        }

def show_resumenes(conexion, id_usuario):
    with conexion.cursor() as cursor:
        query = "SELECT fecha, resumen FROM resumen WHERE id_usuario = %s ORDER BY fecha DESC"
        cursor.execute(query, (id_usuario))
        resumenes = cursor.fetchall()
    return resumenes



def delete_resumenes(conexion, id_usuario, fecha):
    with conexion.cursor() as cursor:
        query = "DELETE FROM resumen WHERE id_usuario = %s AND fecha = %s"
        cursor.execute(query, (id_usuario, fecha))
        conexion.commit()
        return {"eliminado": True, "fecha": fecha}
conexion.close()

import pymysql   # Importamos biblioteca pymysql que nos permitira el manejo de bases de datos MySQL en Python
import backend.clases.diagnostico
import backend.clases.usuario

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
def show_usuario(conexion, user_id, user_pass):

    with conexion.cursor() as cursor:

        query = "SELECT nombre, fecha_nacimiento, tipo_sangre FROM usuario WHERE id_usuario = %s AND  u_password  = %s "
        cursor.execute(query, (user_id,user_pass))
        usuario = cursor.fetchone()

        return usuario
#1.2
def insertar_usuario(conexion,usuario):

    with conexion.cursor() as cursor:

        query = "INSERT INTO usuario (id_usuario,u_password,nombre,fecha_nacimiento,tipo_u,d_especialidad,QR_acceso) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,())
        usuario = cursror.fetcone(usuario.id_usuario, usuario.u_password, usuario.nombre, usuario.fecha_nacimiento, usuario.tipo_u, usuario.d_especialidad, usuario.QR_acceso)

        return usuario
# 2
def show_diagnosticos(conexion):

    with conexion.cursor() as cursor:

        cursor.execute("SELECT * FROM diagnostico;")
        diagnosticos = cursor.fetchall()

        '''for diagnostico in diagnosticos:
            print(diagnostico)
            print('\n')'''

        return diagnosticos
# 2.1
def insertar_diagnostico(conexion,diagnostico):

    with conexion.cursor() as cursor:

        id_medico = diagnostico.id_medico
        id_paciente = diagnostico.id_paciente
        diag = diagnostico.diagIN
        query = "INSERT INTO diagnostico(id_usuario,id_paciente,diagnostico)VALUES (%s,%s,%s)"
        cursor.execute(query,(id_medico,id_paciente,diag))

        conexion.commit()

        return {
                "id_usuario":id_medico, 
                "id_paciente":id_paciente, 
                "diagnostico": diag
                }


        

def show_resumenes(conexion):

    with conexion.cursor() as cursor:

        cursor.execute("SELECT * FROM resumen;")
        resumenes = cursor.fetchall()


        return resumenes

# show_usuarios(conexion)
show_diagnosticos(conexion)


conexion.close()

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

    # 2
def show_diagnosticos(conexion):
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM diagnostico;")
        diagnosticos = cursor.fetchall()

        '''for diagnostico in diagnosticos:
            print('Doctor:',diagnostico[2],'\nDiagnostico:\n',diagnostico[3])
            print('\n')'''

        return diagnosticos


def show_resumenes(conexion):
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM resumen;")
        resumenes = cursor.fetchall()


        return resumenes

# show_usuarios(conexion)
# show_diagnosticos(conexion)


# conexion.close()

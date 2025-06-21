from backend.data.dabatase import conectar
import pymysql


conexion = conectar()

def insert_diagnostico(user_med,user_pac,diag):
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO diagnostico(id_medico,id_usuario,diagnostico) VALUES (",user_med,",",user_pac,",",diag,")")


str1 = input("Insertar nombre de panciente: ")
str2 = input("Insertar diagnostico")

insert_diagnostico('draMeaLoba',str1,str2)

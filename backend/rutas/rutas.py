from flask import Blueprint, jsonify, request
from backend.clases.diagnostico import Diagnostico
from backend.clases.usuario import Usuario
import backend.data.database as db
from datetime import datetime

'''
Utilizando los metodos Blueprint y jsonify se creara el enlace entre el servidor del backend y la base de datos.
21/06/25: Por el momento se tendra un acceso de manera generar, posteriormente cuando se cree el acceso por medio de usuario se filtrara
          la informacion que se mostrara.



'''


front_bp = Blueprint('inicio',__name__)
diagnosticos_bp = Blueprint('diagnosticos', __name__)
usuarios_bp = Blueprint('usuarios', __name__)
resumenes_bp = Blueprint('resumenes', __name__)
login_bp = Blueprint('login',__name__)
diagnosticoInsert_bp = Blueprint('insertDiag',__name__)
insertUsuario_bp = Blueprint('insertUser',__name__)

@front_bp.route('/',methods=['GET'])

def principal():

    return'Sistema web para la gestión y generación automática de resúmenes en expedientes clínicos'


@login_bp.route('/login',methods=['POST'])

def loginUser():

    data = request.get_json()
    user_id = data.get('id_usuario')
    user_pass = data.get('u_password')
    conexion = db.conectar()

    if not all([user_id, user_pass]):
        return jsonify({'error': 'Faltan datos requeridos'}), 400
    
    try:

        usuario = db.show_usuario(conexion,user_id,user_pass)
        return jsonify({"mensaje": "Login exitoso", "usuario": usuario}), 200

    except Exception as e:

        return jsonify({'error': str(e)}), 500



@diagnosticos_bp.route('/diagnosticos', methods=['GET'])

def obtener_diagnosticos():

    try:

        conexion = db.conectar()
        rDiag = db.show_diagnosticos(conexion)
        conexion.close()
        return jsonify(rDiag)  

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@diagnosticoInsert_bp.route('/diagnosticos/entrada',methods=['POST'])

def insertar_diagnostico():

    conexion = db.conectar()
    data = request.get_json()
    id_medico = data.get('id_medico')
    id_paciente = data.get('id_paciente')
    diag = data.get('entradaDiag')

    newDiag = Diagnostico(id_medico,id_paciente,diag)

    if not all([id_medico,id_paciente,diag]):
        return jsonify({'error': 'Faltan datos requeridos'}), 400

    
    try:
        
        entradaDiag = db.insertar_diagnostico(conexion,newDiag)
        return jsonify({"mensaje": "Entrada de datos exitosa", "Diagnostico": entradaDiag}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:

        print(newDiag.__dict__)
        conexion.close()
        


@usuarios_bp.route('/usuarios', methods=['GET'])

def obtener_usuarios():

    try:      

        rConect = db.conectar()
        rUsers = db.show_usuarios(rConect)
        rConect.close()
        return jsonify(rUsers)

    except Exception as e:
        return jsonify({'error': str(e)}),500

@insertUsuario_bp.route('/usuarios/entrada',methods=['POST'])

def insertar_usuarios():

    uConect = db.conectar()
    data = request.get_json()

    id_usuario = data.get('id_usuario')
    u_password = data.get('u_password')
    nombre = data.get('nombre')
    fecha_nacimiento_str = data.get('fecha_nacimiento')
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
    tipo_u = data.get('tipo_u')
    tipo_sangre = data.get('tipo_sangre')
    d_especialidad = data.get('d_especialidad')
    qr_acceso = data.get('qr_acceso')

    newUsuario = Usuario(id_usuario,u_password,nombre,fecha_nacimiento,tipo_u,tipo_sangre,d_especialidad,qr_acceso)

    if not all([id_usuario,u_password,nombre,fecha_nacimiento,tipo_u]):

        return jsonify({'error': 'Faltan datos principales'}), 400

    try:

        entradaUsuario = db.insertar_usuario(uConect,newUsuario)
        return jsonify({"Mensaje":"Alta de usuario exitoso","Usuario":entradaUsuario}),201

    except Exception as e:

        return jsonify({'error': str(e)}), 500

    finally:
        print(fecha_nacimiento_str,'\n',fecha_nacimiento)
        print(newUsuario.__dict__)
        
    uConect.close()



@resumenes_bp.route('/resumenes', methods=['GET'])

def obtener_resumenes():

    try:

        rTest = db.conectar()
        rSumm = db.show_resumenes(rTest)
        rTest.close()
        return jsonify(rSumm)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
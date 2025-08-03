# Dependencias
from flask import Blueprint, jsonify, request
from datetime import datetime

# Clases
from backend.clases.diagnostico import Diagnostico
from backend.clases.usuario import Usuario
from backend.clases.resumen import Resumen

# Herramientas
import backend.herramientas.accesoQR as qrGen
import backend.herramientas.generadorResumen as gRes

# Conexion con base de datos
import backend.data.database as db


# Generacion de blueprint que se exportara ala aplicacion backend
front_bp = Blueprint('inicio',__name__)
diagnosticos_bp = Blueprint('diagnosticos', __name__)
usuarios_bp = Blueprint('usuarios', __name__)
resumenes_bp = Blueprint('resumenes', __name__)
login_bp = Blueprint('login',__name__)
loginQR_bp = Blueprint('loginQR',__name__)
diagnosticoInsert_bp = Blueprint('insertDiag',__name__)
insertUsuario_bp = Blueprint('insertUser',__name__)
insertResumen_bp = Blueprint('insertSummary',__name__)
deleteResumen_bp = Blueprint('deleteSummary',__name__)


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

@loginQR_bp.route('/login/QR',methods=['POST'])

def logQR():
    data = request.get_json()
    qr_acceso = data.get('qr_acceso')

    conexion = db.conectar()


    if not all([qr_acceso]):
        return jsonify({'error': 'Faltan datos requeridos'}), 400
    
    try:

        usuario = db.show_usuarioQR(conexion,qr_acceso)
        return jsonify({"mensaje": "Login exitoso", "usuario": usuario}), 200

    except Exception as e:

        return jsonify({'error': str(e)}), 500

@diagnosticos_bp.route('/diagnosticos', methods=['POST'])

def obtener_diagnosticos():
    data = request.get_json()
    user_id = data.get('id_usuario')

    if not all([user_id]):
        return jsonify({'error': 'Faltan datos requeridos'}), 400
    
    try:

        conexion = db.conectar()
        rDiag = db.show_diagnosticos(conexion,user_id)
        conexion.close()
        return jsonify(rDiag)  

    except Exception as e:
        return jsonify({'error': str(e)}), 500



@diagnosticoInsert_bp.route('/diagnosticos/entrada',methods=['POST'])

def insertar_diagnostico():

    conexion = db.conectar()
    data = request.get_json()
    id_usuario = data.get('id_usuario')
    id_paciente = data.get('id_paciente')
    d_especialidad = data.get('d_especialidad')
    fecha = data.get('fecha')
    diag = data.get('entrada')

    newDiag = Diagnostico(id_usuario,id_paciente,d_especialidad,fecha,diag)

    if not all([id_usuario,id_paciente,fecha,diag]):
        return jsonify({'error': 'Faltan datos requeridos'}), 400

    
    try:
        
        entradaDiag = db.insertar_diagnostico(conexion,newDiag)
        return jsonify({"mensaje": "Entrada de datos exitosa", "Diagnostico": entradaDiag}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:

        # print(newDiag.__dict__)
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
    correo_electronico = data.get('correo_electronico')
    telefono = data.get('telefono')
    pad_Cronico = data.get('pad_Cronico')
    donador_organos = data.get('donador_organos')
    accede_transfucion = data.get('accede_transfucion')
    qr_acceso = qrGen.aleatorizacion(id_usuario,nombre,tipo_sangre)
    qrGen.imagenQR(qr_acceso,id_usuario)

    newUsuario = Usuario(id_usuario,
                        u_password,
                        nombre,
                        fecha_nacimiento,
                        tipo_u,
                        tipo_sangre,
                        d_especialidad,
                        qr_acceso,
                        correo_electronico,
                        telefono,
                        pad_Cronico,
                        donador_organos,
                        accede_transfucion)

    if not all([id_usuario,u_password,nombre,fecha_nacimiento,tipo_u]):

        return jsonify({'error': 'Faltan datos principales'}), 400

    try:

        entradaUsuario = db.insertar_usuario(uConect,newUsuario)
        return jsonify({"Mensaje":"Alta de usuario exitoso","Usuario":entradaUsuario}),201

    except Exception as e:
        print("error de backend: ",e)
        return jsonify({'error': str(e)}), 500

    finally:
        print(fecha_nacimiento_str,'\n',fecha_nacimiento)
        print(newUsuario.__dict__)
        
    uConect.close()



@resumenes_bp.route('/resumenes', methods=['POST'])

def obtener_resumenes():
    try:
        data = request.get_json()
        id_usuario = data.get("id_usuario")

        if not id_usuario:
            return jsonify({"error": "ID de usuario requerido"}), 400

        conexion = db.conectar()
        resumenes = db.show_resumenes(conexion,id_usuario)
        
        return jsonify(resumenes), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@insertResumen_bp.route('/resumenes/entrada', methods=['POST'])
def insertar_resumen():
    try:
        data = request.get_json()
        resumen_texto = data.get("resumen")
        id_usuario = data.get("id_usuario")


        if not resumen_texto or not id_usuario:
            return jsonify({"error": "Resumen e ID de usuario son requeridos"}), 400

        from datetime import date
        conexion = db.conectar()
        fecha = str(date.today())
        
        nuevoResumen = Resumen(id_usuario, fecha, resumen_texto)
        resultado = db.insertar_resumen(conexion, nuevoResumen)
        
        return jsonify({"guardado": True, "datos": resultado}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@insertResumen_bp.route('/resumenes/generar', methods=['POST'])
def generar_resumen():
    try:
        data = request.get_json()
        texto = data.get("texto")

        if not texto:
            return jsonify({"error": "Texto es requerido"}), 400

        resumen = gRes.generadorResumen(texto)

        return jsonify({"resumen": resumen}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@deleteResumen_bp.route('/resumenes/eliminar',methods=['POST'])
def eliminar_resumen():
    try:
        data = request.get_json()
        id_usuario = data.get("id_usuario")
        fecha = data.get("fecha")

        if not id_usuario or not fecha:
            return jsonify({"error": "ID de usuario y fecha son requeridos"}), 400

        conexion = db.conectar()
        resultado = db.delete_resumenes(conexion, id_usuario, fecha)

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
from flask import Blueprint, jsonify
import  backend.data.database as db

'''
Utilizando los metodos Blueprint y jsonify se creara el enlace entre el servidor del backend y la base de datos.
21/06/25: Por el momento se tendra un acceso de manera generar, posteriormente cuando se cree el acceso por medio de usuario se filtrara
          la informacion que se mostrara.



'''


front_bp = Blueprint('inicio',__name__)
diagnosticos_bp = Blueprint('diagnosticos', __name__)
usuarios_bp = Blueprint('usuarios', __name__)
resumenes_bp = Blueprint('resumenes', __name__)


@front_bp.route('/',methods=['GET'])
def principal():
    return'Sistema web para la gestión y generación automática de resúmenes en expedientes clínicos'


@diagnosticos_bp.route('/diagnosticos', methods=['GET'])
def obtener_diagnosticos():
    try:
        conexion = db.conectar()
        rDiag = db.show_diagnosticos(conexion)
        conexion.close()
        return jsonify(rDiag)  
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@usuarios_bp.route('/usuarios', methods=['GET'])
def users_test():
    try:      
        rConect = db.conectar()
        rUsers = db.show_usuarios(rConect)
        rConect.close()
        return jsonify(rUsers)
    except Exception as e:
        return jsonify({'error': str(e)}),500


@resumenes_bp.route('/resumenes', methods=['GET'])
def summary_test():
    try:
        rTest = db.conectar()
        rSumm = db.show_resumenes(rTest)
        rTest.close()
        return jsonify(rSumm)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
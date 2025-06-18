from flask import Flask, jsonify
import pymysql
import data.database as db

app = Flask(__name__)


def conectar_db():
    return pymysql.connect( 
        host="localhost",
        user="vscode_user",
        password="user123",
        database="PI_DB",
        cursorclass = pymysql.cursors.DictCursor  
        )


@app.route('/')
def inicio():
    return 'Prueba'

# Antes de arrancar el proyecto ejecutar venv\Scripts\activate para activar el entorno virtual

@app.route('/diagnosticos', methods=['GET'])
def obtener_diagnosticos():
    try:
        conexion = conectar_db()
        rDiag = db.show_diagnosticos(conexion)
        conexion.close()
        return jsonify(rDiag)  
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/usuarios', methods=['GET'])
def users_test():
    try:      
        rConect = conectar_db()
        rUsers = db.show_usuarios(rConect)
        rConect.close()
        return jsonify(rUsers)
    except Exception as e:
        return jsonify({'error': str(e)}),500


@app.route('/resumenes', methods=['GET'])
def summary_test():
    try:
        rTest = conectar_db()
        rSumm = db.show_resumenes(rTest)
        rTest.close()
        return jsonify(rSumm)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
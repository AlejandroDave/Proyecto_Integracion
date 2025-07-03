from flask import Flask  # Importación de la biblioteca
import backend.rutas.rutas as rutes
'''
Base del Back-End:
Se crea una aplicación Flask cada que se ejecuta la función "crear_app" la cual registrará las rutas indicadas.

'''


def crear_app():
    app = Flask(__name__)

    app.register_blueprint(rutes.front_bp)
    app.register_blueprint(rutes.diagnosticos_bp)
    app.register_blueprint(rutes.usuarios_bp)
    app.register_blueprint(rutes.resumenes_bp)
    app.register_blueprint(rutes.login_bp)
    app.register_blueprint(rutes.diagnosticoInsert_bp)
    app.register_blueprint(rutes.insertUsuario_bp)

    return app


"""
Se creara una condicion que permita crear la aplicacion corroborando que es la aplicación principal.

"""

if __name__ == '__main__':
    app = crear_app()
    app.run(debug=True)
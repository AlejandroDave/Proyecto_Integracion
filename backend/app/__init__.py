from flask import Flask


def crear_app():
    app = Flask(__name__)



    import backend.rutas.rutas as rutes
    
    app.register_blueprint(rutes.front_bp)
    app.register_blueprint(rutes.diagnosticos_bp)
    app.register_blueprint(rutes.usuarios_bp)
    app.register_blueprint(rutes.resumenes_bp)
    app.register_blueprint(rutes.login_bp)
    app.register_blueprint(rutes.diagnosticoInsert_bp)

    return app

if __name__ == '__main__':
    app = crear_app()
    app.run(debug=True)
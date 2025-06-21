from flask import Flask


def crear_app():
    app = Flask(__name__)

    if __name__ == '__main__':
        app.run(debug=True)

    import backend.rutas.rutas as rutes
    
    app.register_blueprint(rutes.front_bp)
    app.register_blueprint(rutes.diagnosticos_bp)
    app.register_blueprint(rutes.usuarios_bp)
    app.register_blueprint(rutes.resumenes_bp)
    return app


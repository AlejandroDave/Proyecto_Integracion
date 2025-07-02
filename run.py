from backend.app import crear_app

app = crear_app() # se invoca la funcion crear_app desde la carpeta app


#Al ser ejecutado se crea la condicion de tener un debug correcto
if __name__ == '__main__':
    app.run(debug=True)
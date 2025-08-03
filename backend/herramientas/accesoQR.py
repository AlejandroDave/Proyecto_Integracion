# import backend.clases.usuario
from pyzbar.pyzbar import decode
from PIL import Image
import qrcode
from random import randint 

def aleatorizacion(id_usuario, nombre, tipo_sangre):
    qr_acceso = ""
    tam = randint(50,100) 

    for _ in range(tam):
        val1 = randint(0, len(id_usuario) - 1)
        val2 = randint(0, len(nombre) - 1)
        val3 = randint(0, len(tipo_sangre) - 1)
        qr_acceso += id_usuario[val1] + nombre[val2] + tipo_sangre[val3]

    return qr_acceso


def decodificar_qr(ruta_imagen):
    try:
        img = Image.open(ruta_imagen)
        datos_decodificados = decode(img)

        if datos_decodificados:
            return datos_decodificados[0].data.decode('utf-8')  # Devuelve como string
        else:
            return "No se detectó ningún código QR en la imagen."
    except Exception as e:
        return f"Error al procesar la imagen: {str(e)}"



def imagenQR(qr_acceso,id_usuario):
    img = qrcode.make(qr_acceso)
    type(img)
    direccion = "./QRAccesos/acceso"+id_usuario+".png"
    img.save(direccion)
    return 1



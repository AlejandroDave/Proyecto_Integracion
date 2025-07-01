from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
#import backend.clases.usuario
from pyzbar.pyzbar import decode
from PIL import Image
import qrcode

'''
30/06/25 Se esta realizando el generador QR que se almancenara de forma encriptada en la base de datos, no se desencriptara por el momento
saludos

'''
class usuario:
    def __init__(self,id_usuario,nombre,fecha_nacimiento):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

# Para funciones academicos se generara una clave por cada ejecucion, para produccion es recomendable almacenar una llave privada

privada = rsa.generate_private_key(  # llave privada para desencriptar
    public_exponent=65537,
    key_size=2048)

publica = privada.public_key()      # llave publica para encriptar


def generarQR(usuario):
    mensajeEnc = b"Usuario: ",usuario.id_usuario,"\nNombre: ",usuario.nombre,"\nFecha de nacimiento: ",usuario.fecha_nacimiento
'''    idUsuario = usuario.id_usuario
    nombreUsuario = usuario.nombre
    userDate = usuario.fecha_nacimiento'''

    encriptado = publica.encrypt(
            mensajeEnc,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))
    img = qrcode.make(encriptado)
    type(img)
    img.save("acceso_",usuario.id_usuario,".png")

    return encriptado


def decodAccesoQR(imagen):
    decodificar = decode(Image.open(imagen))
    print(decodificar)



'''
La función desencriptQR se creó para desencriptar la información previamente encriptada.
Para fines del sistema no será utilizado ya que se almacenará la información encriptada en la base de datos, pero se deja definida
para optimizaciones posteriores.
'''
def desencriptQR(mensaje):
    desencriptado = privada.decrypt(
    mensaje,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None))

    print(desencriptado)

    return desencriptado

userPrueba = usuario("usuario123","Armando Hoyos","1995-04-14")

generarQR(userPrueba)


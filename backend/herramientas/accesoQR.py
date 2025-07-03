from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
#import backend.clases.usuario
from pyzbar.pyzbar import decode
from PIL import Image
import qrcode


img = qrcode.make("mensaje")
type(img)
img.save("acceso_.png")
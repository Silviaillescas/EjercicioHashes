from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

MANIFIESTO = "outputs/SHA256SUMS.txt"
CLAVE_PUBLICA = "outputs/medisoft_pub.pem"
FIRMA = "outputs/SHA256SUMS.sig"

with open(CLAVE_PUBLICA, "rb") as f:
    public_key = RSA.import_key(f.read())

with open(MANIFIESTO, "rb") as f:
    contenido = f.read()

with open(FIRMA, "rb") as f:
    firma = f.read()

hash_obj = SHA256.new(contenido)

try:
    pkcs1_15.new(public_key).verify(hash_obj, firma)
    print("Firma válida")
except (ValueError, TypeError):
    print("Firma inválida")
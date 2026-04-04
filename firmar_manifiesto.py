from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

MANIFIESTO = "outputs/SHA256SUMS.txt"
CLAVE_PRIVADA = "outputs/medisoft_priv.pem"
SALIDA_FIRMA = "outputs/SHA256SUMS.sig"

with open(CLAVE_PRIVADA, "rb") as f:
    private_key = RSA.import_key(f.read())

with open(MANIFIESTO, "rb") as f:
    contenido = f.read()

hash_obj = SHA256.new(contenido)
firma = pkcs1_15.new(private_key).sign(hash_obj)

with open(SALIDA_FIRMA, "wb") as f:
    f.write(firma)

print("Firma generada correctamente:")
print(f" - {SALIDA_FIRMA}")
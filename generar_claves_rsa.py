from Crypto.PublicKey import RSA
import os

os.makedirs("outputs", exist_ok=True)

key = RSA.generate(2048)

private_key = key.export_key()
public_key = key.publickey().export_key()

with open("outputs/medisoft_priv.pem", "wb") as f:
    f.write(private_key)

with open("outputs/medisoft_pub.pem", "wb") as f:
    f.write(public_key)

print("Claves RSA generadas correctamente:")
print(" - outputs/medisoft_priv.pem")
print(" - outputs/medisoft_pub.pem")
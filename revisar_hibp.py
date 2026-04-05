import hashlib
import requests

passwords = [
    "admin",
    "123456",
    "hospital",
    "medisoft2024"
]


def consultar_hibp(password):

    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

    prefijo = sha1[:5]
    sufijo = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefijo}"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error al consultar HIBP para {password}")
        return sha1, None

    hashes = response.text.splitlines()

    for linea in hashes:

        hash_sufijo, cantidad = linea.split(":")

        if hash_sufijo == sufijo:
            return sha1, int(cantidad)

    return sha1, 0


print("\n=== VERIFICACIÓN DE CONTRASEÑAS EN FILTRACIONES ===\n")

for password in passwords:

    sha1, repeticiones = consultar_hibp(password)

    print(f"Contraseña: {password}")
    print(f"SHA-1: {sha1}")

    if repeticiones is None:
        print("No se pudo consultar la API")

    elif repeticiones > 0:
        print(f"Encontrada en filtraciones: {repeticiones} veces")

    else:
        print("No encontrada en filtraciones")

    print("-" * 60)
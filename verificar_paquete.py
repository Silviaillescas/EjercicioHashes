import hashlib
import os

MANIFIESTO = "outputs/SHA256SUMS.txt"

def sha256_archivo(ruta):
    h = hashlib.sha256()

    with open(ruta, "rb") as f:
        while chunk := f.read(4096):
            h.update(chunk)

    return h.hexdigest()

print("\n=== VERIFICACIÓN DE INTEGRIDAD ===\n")

with open(MANIFIESTO, "r", encoding="utf-8") as f:
    lineas = f.readlines()

for linea in lineas:

    hash_esperado, ruta = linea.strip().split(" ", 1)

    if not os.path.exists(ruta):
        print(f"[NO ENCONTRADO] {ruta}")
        continue

    hash_actual = sha256_archivo(ruta)

    if hash_actual == hash_esperado:
        print(f"[OK] {ruta}")

    else:
        print(f"[ALTERADO] {ruta}")
        print(f"  Esperado: {hash_esperado}")
        print(f"  Actual:   {hash_actual}")
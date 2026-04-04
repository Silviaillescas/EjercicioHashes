import hashlib
import os

CARPETA = "paquete_medisoft"
SALIDA = "outputs/SHA256SUMS.txt"

def sha256_archivo(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()

os.makedirs("outputs", exist_ok=True)

archivos = sorted(os.listdir(CARPETA))

with open(SALIDA, "w", encoding="utf-8") as out:
    for nombre in archivos:
        ruta = os.path.join(CARPETA, nombre)
        if os.path.isfile(ruta):
            hash_hex = sha256_archivo(ruta)
            out.write(f"{hash_hex} {ruta}\n")
            print(f"{nombre}: {hash_hex}")

print(f"\nManifiesto generado en: {SALIDA}")
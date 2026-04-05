import hashlib


def calcular_hashes(texto):
    data = texto.encode("utf-8")
    resultados = {
        "MD5": hashlib.md5(data).hexdigest(),
        "SHA-1": hashlib.sha1(data).hexdigest(),
        "SHA-256": hashlib.sha256(data).hexdigest(),
        "SHA3-256": hashlib.sha3_256(data).hexdigest(),
    }
    return resultados


def contar_bits_distintos(hash1, hash2):
    xor_resultado = int(hash1, 16) ^ int(hash2, 16)
    return bin(xor_resultado).count("1")


texto_1 = "MediSoft-v2.1.0"
texto_2 = "medisoft-v2.1.0"

hashes_1 = calcular_hashes(texto_1)
hashes_2 = calcular_hashes(texto_2)

print("\n=== TABLA COMPARATIVA DE HASHES ===\n")
print(f"{'Texto':20} {'Algoritmo':10} {'Bits':6} {'Hex':6} {'Valor hash'}")
print("-" * 120)

for algoritmo, valor in hashes_1.items():
    bits = len(valor) * 4
    longitud_hex = len(valor)
    print(f"{texto_1:20} {algoritmo:10} {bits:<6} {longitud_hex:<6} {valor}")

for algoritmo, valor in hashes_2.items():
    bits = len(valor) * 4
    longitud_hex = len(valor)
    print(f"{texto_2:20} {algoritmo:10} {bits:<6} {longitud_hex:<6} {valor}")

sha256_1 = hashes_1["SHA-256"]
sha256_2 = hashes_2["SHA-256"]

bits_cambiados = contar_bits_distintos(sha256_1, sha256_2)

print("\n=== ANÁLISIS SHA-256 ===")
print(f"SHA-256 de '{texto_1}': {sha256_1}")
print(f"SHA-256 de '{texto_2}': {sha256_2}")
print(f"Bits diferentes entre ambos hashes: {bits_cambiados}")
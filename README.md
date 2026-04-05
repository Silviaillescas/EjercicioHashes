# Ejercicio: Hashes y Firmas Digitales

## Descripción

En este laboratorio se implementan mecanismos criptográficos para proteger la integridad y autenticidad de archivos distribuidos por una empresa ficticia llamada MediSoft S.A., la cual desarrolla software de diagnóstico para hospitales.

El objetivo principal es demostrar cómo las funciones hash y las firmas digitales permiten detectar modificaciones no autorizadas en archivos y garantizar que los datos provienen de una fuente legítima.

Se implementaron las siguientes funcionalidades:

- Comparación de algoritmos hash (MD5, SHA-1, SHA-256 y SHA3-256)
- Consulta de contraseñas filtradas usando la API de Have I Been Pwned
- Generación de un manifiesto de integridad usando SHA-256
- Verificación de integridad de archivos
- Generación de claves RSA
- Firma digital del manifiesto
- Verificación de autenticidad mediante firma digital

---

## Estructura del proyecto

```
Ejercicio-Hashes-Firmas/
│
├── explorar_hashes.py
├── revisar_hibp.py
├── generar_manifiesto.py
├── verificar_paquete.py
├── generar_claves_rsa.py
├── firmar_manifiesto.py
├── verificar_firma.py
│
├── requirements.txt
├── README.md
│
├── paquete_medisoft/
│   ├── configuracion_equipo.txt
│   ├── parametros_laboratorio.json
│   ├── registro_sistema.log
│   ├── actualizacion_medisoft_v2.1.0.zip
│   └── manual_tecnico.pdf
│
└── outputs/
    ├── SHA256SUMS.txt
    ├── SHA256SUMS.sig
    ├── medisoft_priv.pem
    └── medisoft_pub.pem
```

---

## Instalación

Instalar dependencias:

```
pip install -r requirements.txt
```

Dependencias utilizadas:

- pycryptodome
- requests

---

## Ejecución de los scripts

### 1. Comparación de hashes

```
python explorar_hashes.py
```

Genera una tabla comparativa entre MD5, SHA-1, SHA-256 y SHA3-256 para dos textos similares.

---

### 2. Consulta de contraseñas filtradas

```
python revisar_hibp.py
```

Consulta si contraseñas comunes aparecen en filtraciones públicas utilizando la API de Have I Been Pwned.

---

### 3. Generación del manifiesto de integridad

```
python generar_manifiesto.py
```

Genera el archivo:

```
outputs/SHA256SUMS.txt
```

que contiene el hash SHA-256 de cada archivo del paquete.

---

### 4. Verificación de integridad del paquete

```
python verificar_paquete.py
```

Compara los hashes actuales de los archivos con los registrados en el manifiesto.

---

### 5. Generación de claves RSA

```
python generar_claves_rsa.py
```

Genera:

```
outputs/medisoft_priv.pem
outputs/medisoft_pub.pem
```

---

### 6. Firma digital del manifiesto

```
python firmar_manifiesto.py
```

Genera:

```
outputs/SHA256SUMS.sig
```

---

### 7. Verificación de firma digital

```
python verificar_firma.py
```

Valida que el manifiesto no haya sido modificado desde que fue firmado.

---

## Ejemplos de ejecución

### Verificación de integridad correcta

```
[OK] paquete_medisoft/configuracion_equipo.txt
[OK] paquete_medisoft/parametros_laboratorio.json
[OK] paquete_medisoft/registro_sistema.log
[OK] paquete_medisoft/actualizacion_medisoft_v2.1.0.zip
[OK] paquete_medisoft/manual_tecnico.pdf
```

---

### Archivo alterado

Después de modificar un archivo:

```
[ALTERADO] paquete_medisoft/configuracion_equipo.txt
```

Esto demuestra que el hash cambia aunque la modificación sea mínima.

---

### Firma válida

```
Firma válida
```

---

### Firma inválida al modificar el manifiesto

```
Firma inválida
```

---

## Respuestas de análisis

### 1. ¿Cuántos bits cambiaron entre los dos hashes SHA-256? ¿Qué propiedad demuestra?

Al comparar los hashes SHA-256 de los textos:

- "MediSoft-v2.1.0"
- "medisoft-v2.1.0"

se observa que cambian muchos bits a pesar de que solo se modificó una letra en el texto original.

Esto demuestra la propiedad de efecto avalancha, la cual indica que un pequeño cambio en la entrada produce un cambio completamente diferente en la salida del hash.

Esta propiedad es fundamental para la seguridad criptográfica, ya que evita que sea posible predecir cómo cambiará el hash al modificar el mensaje original.

---

### 2. ¿Por qué MD5 es considerado inseguro para integridad de archivos?

MD5 produce hashes de 128 bits y presenta vulnerabilidades conocidas relacionadas con colisiones.

Una colisión ocurre cuando dos archivos diferentes generan el mismo hash.

Esto permite que un atacante pueda modificar un archivo sin cambiar su hash MD5, lo que compromete la integridad del sistema.

Debido a estas debilidades, MD5 ya no se considera seguro para verificar integridad de archivos en sistemas modernos.

SHA-256 es más seguro porque produce hashes de 256 bits y no presenta colisiones prácticas conocidas.

---

### 3. ¿Por qué SHA-256 directo sobre contraseñas es inseguro?

El uso de SHA-256 directamente sobre contraseñas es inseguro porque existen bases de datos públicas que contienen millones de hashes de contraseñas comunes.

La consulta realizada mediante la API Have I Been Pwned demuestra que contraseñas simples como "admin" o "123456" aparecen miles o millones de veces en filtraciones.

Esto significa que un atacante puede comparar el hash de una contraseña con bases de datos existentes y descubrir la contraseña original.

Por esta razón, se recomienda utilizar algoritmos diseñados específicamente para contraseñas como:

- Argon2id
- bcrypt
- scrypt

Estos algoritmos utilizan salt y son computacionalmente más costosos, lo que dificulta ataques de fuerza bruta.

---

### 4. ¿Por qué la firma es válida después de modificar un archivo del paquete?

La firma digital se realiza sobre el archivo:

```
SHA256SUMS.txt
```

Este archivo contiene los hashes originales de los archivos del paquete.

Si un archivo del paquete es modificado después de haber generado el manifiesto, la firma sigue siendo válida porque el contenido del manifiesto no ha cambiado.

Sin embargo, al ejecutar el script de verificación de integridad, el sistema detecta que el hash actual del archivo no coincide con el hash registrado en el manifiesto.

Esto demuestra que:

la firma digital garantiza la autenticidad del manifiesto, mientras que la función hash garantiza la integridad de los archivos.

Ambos mecanismos trabajan juntos para asegurar la seguridad del sistema.

---

## Conclusiones

Las funciones hash permiten verificar la integridad de los archivos, ya que cualquier modificación en el contenido produce un hash completamente diferente.

El efecto avalancha demuestra que incluso cambios mínimos en los datos generan resultados impredecibles, lo que fortalece la seguridad criptográfica.

El uso de SHA-256 proporciona mayor seguridad que MD5 debido a su mayor longitud y resistencia a colisiones.

El uso de firmas digitales con RSA permite garantizar que el manifiesto de hashes proviene realmente de la fuente legítima, evitando que un atacante pueda modificar tanto los archivos como los hashes sin ser detectado.

Finalmente, el análisis de contraseñas filtradas demuestra la importancia de utilizar algoritmos especializados como Argon2id para proteger credenciales de usuario.

---

## Uso de Inteligencia Artificial

Durante el desarrollo de este laboratorio utilicé inteligencia artificial (Chat GPT) como apoyo para aclarar dudas y reforzar algunos conceptos relacionados con funciones hash, verificación de integridad y firmas digitales. La IA me ayudó principalmente a comprender mejor la lógica de implementación en Python y a validar que los pasos realizados fueran correctos.

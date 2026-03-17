from faker import Faker
import random


datos_ficticios = Faker("es_ES")

diccionario_usuarios = {}

for codigo in range(1, 16):
    diccionario_usuarios[codigo] = {
        "nome": datos_ficticios.name(),
        "direccion": datos_ficticios.address(),
        "correo_electronico": datos_ficticios.email(),
        "telefono": datos_ficticios.phone_number(),
    }

print("Os usuarios son os seguintes:")

for codigo, usuario in diccionario_usuarios.items():
    direccion = usuario["direccion"].replace("\n", " ").replace("  ", " ")
    print(
        f"Usuario nº {codigo} -> Nome: {usuario['nome']}, "
        f"Dirección: {direccion}, "
        f"Correo electrónico: {usuario['correo_electronico']}, "
        f"Teléfono: {usuario['telefono']}"
    )

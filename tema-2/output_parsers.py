# libreria para validacion de datos
from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nombre: str
    activo: bool = True

data = {
    "id": 123,
    "nombre": "Jose",
    "activo": True,
}

# usuario = Usuario(id=123, nombre="Jose", activo=True)
usuario = Usuario(**data)

print(usuario)
print(usuario.model_dump_json())
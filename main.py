from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API Básica en Memoria")

# 1. Base de datos simulada (Listas)
db_usuarios = []
db_libros = []

# 2. Modelos de datos
class Usuario(BaseModel):
    id: int
    nombre: str
    email: str

class Libro(BaseModel):
    id: int
    titulo: str
    autor: str

# 3. CRUD para Usuarios
@app.post("/usuarios/", response_model=Usuario)
def crear_usuario(usuario: Usuario):
    # Verificamos si el ID ya existe
    if any(u.id == usuario.id for u in db_usuarios):
        raise HTTPException(status_code=400, detail="El ID ya existe")
    db_usuarios.append(usuario)
    return usuario

@app.get("/usuarios/", response_model=List[Usuario])
def leer_usuarios():
    return db_usuarios

@app.delete("/usuarios/{usuario_id}")
def borrar_usuario(usuario_id: int):
    global db_usuarios
    db_usuarios = [u for u in db_usuarios if u.id != usuario_id]
    return {"mensaje": "Usuario eliminado"}

# 4. CRUD para Libros
@app.post("/libros/", response_model=Libro)
def crear_libro(libro: Libro):
    if any(l.id == libro.id for l in db_libros):
        raise HTTPException(status_code=400, detail="El ID ya existe")
    db_libros.append(libro)
    return libro

@app.get("/libros/", response_model=List[Libro])
def leer_libros():
    return db_libros

@app.delete("/libros/{libro_id}")
def borrar_libro(libro_id: int):
    global db_libros
    db_libros = [l for l in db_libros if l.id != libro_id]
    return {"mensaje": "Libro eliminado"}
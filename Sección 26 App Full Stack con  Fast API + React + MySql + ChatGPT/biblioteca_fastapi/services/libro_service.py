from sqlalchemy.orm import Session

from models.libro import Libro

from schemas import LibroCreate
from schemas import LibroUpdate


# =========================================================
# Función listar_libros
# =========================================================
# Retorna todos los libros registrados
# en la base de datos.
# =========================================================
def listar_libros(db: Session):

    libros = db.query(Libro).all()

    return libros


# =========================================================
# Función crear_libro
# =========================================================
# Crea un nuevo libro en MySQL.
# =========================================================
def crear_libro(
    db: Session,
    datos: LibroCreate
):

    nuevo_libro = Libro(
        titulo=datos.titulo,
        autor=datos.autor,
        rating=datos.rating
    )

    db.add(nuevo_libro)

    db.commit()

    db.refresh(nuevo_libro)

    return nuevo_libro


# =========================================================
# Función obtener_libro_por_id
# =========================================================
# Busca un libro usando su id.
# =========================================================
def obtener_libro_por_id(
    db: Session,
    id: int
):

    libro = (
        db.query(Libro)
        .filter(Libro.id == id)
        .first()
    )

    return libro


# =========================================================
# Función actualizar_libro
# =========================================================
# Actualiza un libro existente.
# =========================================================
def actualizar_libro(
    db: Session,
    id: int,
    datos: LibroUpdate
):

    libro = obtener_libro_por_id(
        db,
        id
    )

    if libro is None:
        return None

    datos_actualizados = datos.model_dump(
        exclude_unset=True
    )

    for campo, valor in datos_actualizados.items():
        setattr(libro, campo, valor)

    db.commit()

    db.refresh(libro)

    return libro


# [NUEVO]
# =========================================================
# Función eliminar_libro
# =========================================================
# Esta función:
# - busca el libro por id
# - elimina el registro
# - guarda cambios en MySQL
#
# Retorna:
# - Libro eliminado
# - None si no existe
# =========================================================
def eliminar_libro(
    db: Session,
    id: int
):

    # =====================================================
    # Buscar libro
    # =====================================================
    libro = obtener_libro_por_id(
        db,
        id
    )

    # =====================================================
    # Validar existencia
    # =====================================================
    if libro is None:
        return None

    # =====================================================
    # Eliminar registro
    # =====================================================
    db.delete(libro)

    # =====================================================
    # Guardar cambios
    # =====================================================
    db.commit()

    # =====================================================
    # Retornar libro eliminado
    # =====================================================
    return libro
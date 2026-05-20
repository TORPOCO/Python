from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Path
from fastapi import status

from sqlalchemy.orm import Session

from database import get_db

from schemas import LibroCreate
from schemas import LibroRead
from schemas import LibroUpdate

from services.libro_service import listar_libros
from services.libro_service import crear_libro
from services.libro_service import obtener_libro_por_id
from services.libro_service import actualizar_libro

# [NUEVO]
from services.libro_service import eliminar_libro


# =========================================================
# Router de libros
# =========================================================
router = APIRouter(
    prefix="/api/libros",
    tags=["Libros"]
)


# =========================================================
# Endpoint: listar libros
# =========================================================
# GET /api/libros
# =========================================================
@router.get(
    "",
    response_model=List[LibroRead]
)
def obtener_libros(
    db: Session = Depends(get_db)
):

    libros = listar_libros(db)

    return libros


# =========================================================
# Endpoint: crear libro
# =========================================================
# POST /api/libros
# =========================================================
@router.post(
    "",
    response_model=LibroRead,
    status_code=status.HTTP_201_CREATED
)
def crear_nuevo_libro(
    datos: LibroCreate,
    db: Session = Depends(get_db)
):

    nuevo_libro = crear_libro(
        db,
        datos
    )

    return nuevo_libro


# =========================================================
# Endpoint: obtener libro por id
# =========================================================
# GET /api/libros/{id}
# =========================================================
@router.get(
    "/{id}",
    response_model=LibroRead
)
def obtener_libro(
    id: int = Path(
        ...,
        gt=0,
        description="ID del libro"
    ),

    db: Session = Depends(get_db)
):

    libro = obtener_libro_por_id(
        db,
        id
    )

    if libro is None:

        raise HTTPException(
            status_code=404,
            detail="Libro no encontrado"
        )

    return libro


# =========================================================
# Endpoint: actualizar libro
# =========================================================
# PUT /api/libros/{id}
# =========================================================
@router.put(
    "/{id}",
    response_model=LibroRead
)
def actualizar_libro_endpoint(

    id: int = Path(
        ...,
        gt=0,
        description="ID del libro"
    ),

    datos: LibroUpdate = ...,

    db: Session = Depends(get_db)
):

    libro_actualizado = actualizar_libro(
        db,
        id,
        datos
    )

    if libro_actualizado is None:

        raise HTTPException(
            status_code=404,
            detail="Libro no encontrado"
        )

    return libro_actualizado


# [NUEVO]
# =========================================================
# Endpoint: eliminar libro
# =========================================================
# DELETE /api/libros/{id}
#
# Elimina un libro existente.
# =========================================================
@router.delete(
    "/{id}"
)
def eliminar_libro_endpoint(

    # =====================================================
    # ID recibido desde URL
    # =====================================================
    id: int = Path(
        ...,
        gt=0,
        description="ID del libro"
    ),

    db: Session = Depends(get_db)
):

    # =====================================================
    # Intentar eliminar libro
    # =====================================================
    libro_eliminado = eliminar_libro(
        db,
        id
    )

    # =====================================================
    # Validar existencia
    # =====================================================
    if libro_eliminado is None:

        raise HTTPException(
            status_code=404,
            detail="Libro no encontrado"
        )

    # =====================================================
    # Respuesta simple
    # =====================================================
    return {
        "mensaje": "Libro eliminado correctamente"
    }
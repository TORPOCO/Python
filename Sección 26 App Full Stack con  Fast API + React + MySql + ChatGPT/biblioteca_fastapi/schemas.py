from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


# =========================================================
# Esquema base para Libro
# =========================================================
# Contiene los campos comunes:
# - titulo
# - autor
# - rating
#
# Este esquema será reutilizado por:
# - LibroCreate
# - LibroUpdate
# =========================================================
class LibroBase(BaseModel):

    # =====================================================
    # Título del libro
    # =====================================================
    # min_length=1 evita cadenas vacías.
    # =====================================================
    titulo: str = Field(
        ...,
        min_length=1,
        description="Título del libro"
    )

    # =====================================================
    # Autor del libro
    # =====================================================
    autor: str = Field(
        ...,
        min_length=1,
        description="Autor del libro"
    )

    # =====================================================
    # Rating del libro
    # =====================================================
    # ge = greater or equal
    # le = less or equal
    #
    # Permite solo valores entre 1 y 5.
    # =====================================================
    rating: int = Field(
        ...,
        ge=1,
        le=5,
        description="Rating entre 1 y 5"
    )


# =========================================================
# Esquema para creación
# =========================================================
# Hereda todos los campos obligatorios
# desde LibroBase.
# =========================================================
class LibroCreate(LibroBase):
    pass


# =========================================================
# Esquema para actualización
# =========================================================
# Los campos son opcionales para permitir
# actualizaciones parciales.
# =========================================================
class LibroUpdate(BaseModel):

    titulo: Optional[str] = Field(
        None,
        min_length=1,
        description="Nuevo título"
    )

    autor: Optional[str] = Field(
        None,
        min_length=1,
        description="Nuevo autor"
    )

    rating: Optional[int] = Field(
        None,
        ge=1,
        le=5,
        description="Nuevo rating"
    )


# =========================================================
# Esquema de lectura / respuesta
# =========================================================
# Este esquema representa lo que devolverá
# la API al cliente.
#
# Incluye:
# - id
# - titulo
# - autor
# - rating
# =========================================================
class LibroRead(LibroBase):

    id: int

    # =====================================================
    # Configuración Pydantic v2
    # =====================================================
    # Permite convertir automáticamente
    # modelos SQLAlchemy a respuestas JSON.
    # =====================================================
    model_config = ConfigDict(
        from_attributes=True
    )
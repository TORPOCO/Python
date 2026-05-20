from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from database import Base


# =========================================================
# Modelo Libro
# =========================================================
# Esta clase representa la tabla "libros"
# dentro de la base de datos MySQL.
#
# Cada atributo de la clase representa
# una columna de la tabla.
# =========================================================
class Libro(Base):

    # =====================================================
    # Nombre de la tabla en MySQL
    # =====================================================
    __tablename__ = "libros"

    # =====================================================
    # ID del libro
    # =====================================================
    # - Llave primaria
    # - Entero autoincremental
    # =====================================================
    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    # =====================================================
    # Título del libro
    # =====================================================
    # nullable=False indica que el campo es obligatorio.
    # =====================================================
    titulo = Column(
        String(255),
        nullable=False
    )

    # =====================================================
    # Autor del libro
    # =====================================================
    autor = Column(
        String(255),
        nullable=False
    )

    # =====================================================
    # Rating del libro
    # =====================================================
    # Valor entero entre 1 y 5.
    #
    # Más adelante validaremos esto
    # con Pydantic.
    # =====================================================
    rating = Column(
        Integer,
        nullable=False
    )
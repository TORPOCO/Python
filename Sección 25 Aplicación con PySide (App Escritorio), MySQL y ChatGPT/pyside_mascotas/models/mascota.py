from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from database import Base


# =========================================================
# Modelo Mascota
# =========================================================
# Representa la tabla "mascotas" en MySQL
class Mascota(Base):

    # Nombre de la tabla en la base de datos
    __tablename__ = "mascotas"

    # =========================================================
    # Columnas de la tabla
    # =========================================================

    # ID autoincremental
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    # Nombre de la mascota
    nombre = Column(
        String(100),
        nullable=False
    )

    # Especie de la mascota
    especie = Column(
        String(100),
        nullable=False
    )

    # Peso en kilogramos
    peso = Column(
        Float,
        nullable=False
    )
import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy import text

from alembic.config import Config
from alembic import command


# =========================================================
# Cargar variables del .env
# =========================================================
load_dotenv()


# =========================================================
# Construir URL de conexión
# =========================================================
DATABASE_URL = (
    f"mysql+pymysql://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)


# =========================================================
# Crear engine temporal
# =========================================================
engine = create_engine(DATABASE_URL)


# =========================================================
# Limpiar alembic_version huérfana si existe
# =========================================================
# Esto ayuda cuando:
# - se borraron migraciones manualmente
# - existe inconsistencia de versiones
# =========================================================
with engine.connect() as connection:

    try:
        connection.execute(
            text("DROP TABLE IF EXISTS alembic_version")
        )

        connection.commit()

        print("✅ Tabla alembic_version limpiada")

    except Exception as error:
        print("⚠️ No se pudo limpiar alembic_version")
        print(error)


# =========================================================
# Configurar Alembic
# =========================================================
alembic_cfg = Config("alembic.ini")


# =========================================================
# Generar migración automática
# =========================================================
try:

    command.revision(
        alembic_cfg,
        autogenerate=True,
        message="crear tabla libros"
    )

    print("✅ Migración generada")

except Exception as error:
    print("⚠️ Error generando migración")
    print(error)


# =========================================================
# Aplicar migración
# =========================================================
try:

    command.upgrade(
        alembic_cfg,
        "head"
    )

    print("✅ Migración aplicada correctamente")

except Exception as error:
    print("❌ Error aplicando migración")
    print(error)
import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy import text

from alembic.config import Config
from alembic import command


# =========================================================
# Cargar variables de entorno
# =========================================================
load_dotenv()


# =========================================================
# Construcción de URL de conexión
# =========================================================
DATABASE_URL = (
    f"mysql+pymysql://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASS')}"
    f"@{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)


# =========================================================
# Crear engine
# =========================================================
engine = create_engine(DATABASE_URL)


# =========================================================
# Configuración Alembic
# =========================================================
alembic_cfg = Config("alembic.ini")


# =========================================================
# Limpiar alembic_version huérfana si existe
# =========================================================
try:

    with engine.connect() as connection:

        result = connection.execute(
            text(
                """
                SHOW TABLES LIKE 'alembic_version'
                """
            )
        )

        table_exists = result.fetchone()

        if table_exists:

            result = connection.execute(
                text(
                    """
                    SELECT version_num
                    FROM alembic_version
                    """
                )
            )

            version = result.fetchone()

            versions_path = "alembic/versions"

            if version:

                version_file_exists = False

                for filename in os.listdir(versions_path):

                    if version[0] in filename:
                        version_file_exists = True
                        break

                # =========================================================
                # Si no existe el archivo de versión, limpiar tabla
                # =========================================================
                if not version_file_exists:

                    print(
                        "⚠️ alembic_version huérfana detectada"
                    )

                    connection.execute(
                        text(
                            """
                            DROP TABLE alembic_version
                            """
                        )
                    )

                    connection.commit()

                    print(
                        "🧹 Tabla alembic_version eliminada"
                    )

except Exception as error:

    print("❌ Error verificando alembic_version")
    print(error)


# =========================================================
# Generar migración automática
# =========================================================
print("🛠 Generando migración automática...")

command.revision(
    alembic_cfg,
    autogenerate=True,
    message="crear tabla mascotas"
)


# =========================================================
# Aplicar migraciones
# =========================================================
print("⬆ Aplicando migraciones...")

command.upgrade(
    alembic_cfg,
    "head"
)


print("✅ Migración completada")
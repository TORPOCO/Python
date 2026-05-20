import os
import subprocess

from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, text


load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASS}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)


def limpiar_alembic_version():
    try:
        inspector = inspect(engine)

        tablas = inspector.get_table_names()

        if "alembic_version" in tablas:
            with engine.connect() as connection:
                connection.execute(
                    text("DROP TABLE alembic_version")
                )
                connection.commit()

            print("🧹 Tabla alembic_version eliminada")

    except Exception as error:
        print("⚠️ Error revisando alembic_version:")
        print(error)


def crear_migracion():
    try:
        print("🛠️ Generando migración automática...")

        subprocess.run(
            [
                "alembic",
                "revision",
                "--autogenerate",
                "-m",
                "crear tabla peliculas"
            ],
            check=True
        )

        print("✅ Migración generada correctamente")

    except Exception as error:
        print("❌ Error generando migración:")
        print(error)


def aplicar_migracion():
    try:
        print("⬆️ Aplicando migraciones...")

        subprocess.run(
            [
                "alembic",
                "upgrade",
                "head"
            ],
            check=True
        )

        print("✅ Migraciones aplicadas correctamente")

    except Exception as error:
        print("❌ Error aplicando migraciones:")
        print(error)


if __name__ == "__main__":
    print("🚀 Iniciando proceso de migración")

    limpiar_alembic_version()

    crear_migracion()

    aplicar_migracion()

    print("🎉 Proceso finalizado")
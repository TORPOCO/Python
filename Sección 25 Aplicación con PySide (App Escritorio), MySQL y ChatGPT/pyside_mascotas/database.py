import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# =========================================================
# Cargar variables de entorno desde .env
# =========================================================
load_dotenv()


# =========================================================
# Obtener variables de entorno
# =========================================================
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


# =========================================================
# Construcción de la URL de conexión
# =========================================================
DATABASE_URL = (
    f"mysql+pymysql://"
    f"{DB_USER}:{DB_PASS}"
    f"@{DB_HOST}:{DB_PORT}"
    f"/{DB_NAME}"
)


# =========================================================
# Crear engine de SQLAlchemy
# =========================================================
engine = create_engine(
    DATABASE_URL,
    echo=True
)


# =========================================================
# Crear fábrica de sesiones
# =========================================================
Session = sessionmaker(
    bind=engine
)


# =========================================================
# Base para modelos ORM
# =========================================================
Base = declarative_base()


# =========================================================
# Prueba de conexión
# =========================================================
if __name__ == "__main__":

    try:
        # Abrir conexión
        with engine.connect() as connection:

            print("✅ Conexión exitosa a MySQL")
            print(connection)

    except Exception as error:

        print("❌ Error al conectar con MySQL")
        print(error)
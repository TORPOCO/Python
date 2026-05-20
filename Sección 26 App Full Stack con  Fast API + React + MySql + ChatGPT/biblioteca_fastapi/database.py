import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


# =========================================================
# Cargar variables del archivo .env
# =========================================================
# Esto permite acceder a:
# - usuario
# - password
# - host
# - puerto
# - nombre de la base de datos
# =========================================================
load_dotenv()


# =========================================================
# Leer variables de entorno
# =========================================================
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


# =========================================================
# Construir URL de conexión MySQL
# =========================================================
# Formato:
# mysql+pymysql://usuario:password@host:puerto/basedatos
# =========================================================
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


# =========================================================
# Crear motor de conexión SQLAlchemy
# =========================================================
# El engine administra las conexiones con la BD.
# =========================================================
engine = create_engine(
    DATABASE_URL,
    echo=True
)


# =========================================================
# Crear fábrica de sesiones
# =========================================================
# SessionLocal creará sesiones independientes
# para cada petición HTTP.
# =========================================================
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)


# =========================================================
# Base para modelos ORM
# =========================================================
# Todas las clases modelo heredarán de Base.
# =========================================================
Base = declarative_base()


# =========================================================
# Dependencia get_db()
# =========================================================
# Esta función:
# - abre una sesión
# - la entrega al endpoint
# - la cierra automáticamente
#
# FastAPI usará esto con Depends(get_db)
# =========================================================
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# =========================================================
# Prueba rápida de conexión
# =========================================================
# Permite verificar si la conexión funciona:
#
# python database.py
# =========================================================
if __name__ == "__main__":

    try:
        with engine.connect():
            print("✅ Conexión a MySQL exitosa")

    except Exception as error:
        print("❌ Error de conexión:")
        print(error)
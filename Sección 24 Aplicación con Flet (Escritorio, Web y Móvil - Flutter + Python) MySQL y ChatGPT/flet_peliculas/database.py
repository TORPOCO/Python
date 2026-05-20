import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker


# Cargar variables de entorno
load_dotenv()

# Obtener variables del .env
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Construir URL de conexión
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASS}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Crear engine de conexión
engine = create_engine(
    DATABASE_URL,
    echo=True
)

# Crear sesiones
Session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# Clase base para modelos
Base = declarative_base()


# Prueba de conexión
def probar_conexion():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        print("✅ Conexión exitosa con MySQL")

    except Exception as error:
        print("❌ Error de conexión:")
        print(error)


if __name__ == "__main__":
    probar_conexion()
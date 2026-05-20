from fastapi import FastAPI

# [NUEVO]
from fastapi.middleware.cors import CORSMiddleware

# [NUEVO]
from api.libros import router as libros_router


# =========================================================
# Crear aplicación FastAPI
# =========================================================
app = FastAPI(
    title="API Biblioteca Personal"
)


# [NUEVO]
# =========================================================
# Configuración CORS
# =========================================================
#
# Permite que frontends externos
# puedan consumir esta API.
#
# React Vite:
# http://localhost:5173
#
# Angular:
# http://localhost:4200
# =========================================================
origins = [
    "http://localhost:4200",
    "http://localhost:5173",
]


# [NUEVO]
# =========================================================
# Agregar middleware CORS
# =========================================================
app.add_middleware(
    CORSMiddleware,

    # Orígenes permitidos
    allow_origins=origins,

    # Permitir cookies/autenticación
    allow_credentials=True,

    # Métodos HTTP permitidos
    allow_methods=["*"],

    # Headers permitidos
    allow_headers=["*"],
)


# [NUEVO]
# =========================================================
# Registrar router de libros
# =========================================================
app.include_router(libros_router)


# =========================================================
# Endpoint de prueba
# =========================================================
@app.get("/")
def root():

    return {
        "mensaje": "API Biblioteca funcionando correctamente"
    }
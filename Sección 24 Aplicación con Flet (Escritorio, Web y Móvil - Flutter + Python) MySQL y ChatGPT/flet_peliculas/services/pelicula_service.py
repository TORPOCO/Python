from database import Session
from models.pelicula import Pelicula

# [NUEVO]
def validar_datos(datos):

    if not datos["titulo"].strip():
        return "El título es obligatorio"

    if not datos["director"].strip():
        return "El director es obligatorio"

    if not datos["puntuacion"].strip():
        return "La puntuación es obligatoria"

    try:
        puntuacion = int(datos["puntuacion"])

    except ValueError:
        return "La puntuación debe ser un número entero"

    if puntuacion < 1 or puntuacion > 10:
        return "La puntuación debe estar entre 1 y 10"

    return None

def obtener_todos():
    session = Session()

    try:
        peliculas = session.query(Pelicula).all()
        return peliculas

    except Exception as error:
        print("❌ Error obteniendo películas:")
        print(error)
        return []

    finally:
        session.close()


# [NUEVO]
def crear(datos):
    session = Session()

    try:
        # [MODIFICADO]
        error = validar_datos(datos)

        if error:
            return {
                "ok": False,
                "mensaje": error
            }

        puntuacion = int(datos["puntuacion"])

        if puntuacion < 1 or puntuacion > 10:
            return {
                "ok": False,
                "mensaje": "La puntuación debe estar entre 1 y 10"
            }

        pelicula = Pelicula(
            titulo=datos["titulo"],
            director=datos["director"],
            puntuacion=puntuacion
        )

        session.add(pelicula)

        session.commit()

        return {
            "ok": True,
            "mensaje": "🎉 Película creada correctamente"
        }

    except Exception as error:
        session.rollback()

        print("❌ Error creando película:")
        print(error)

        return {
            "ok": False,
            "mensaje": "Ocurrió un error al guardar"
        }

    finally:
        session.close()


# [NUEVO]
def obtener_por_id(id):
    session = Session()

    try:
        pelicula = (
            session.query(Pelicula)
            .filter(Pelicula.id == id)
            .first()
        )

        return pelicula

    except Exception as error:
        print("❌ Error obteniendo película por ID:")
        print(error)

        return None

    finally:
        session.close()

# [NUEVO]
def actualizar(id, datos):
    session = Session()

    try:
        pelicula = (
            session.query(Pelicula)
            .filter(Pelicula.id == id)
            .first()
        )

        if not pelicula:
            return {
                "ok": False,
                "mensaje": "Película no encontrada"
            }

        # [MODIFICADO]
        error = validar_datos(datos)

        if error:
            return {
                "ok": False,
                "mensaje": error
            }

        puntuacion = int(datos["puntuacion"])

        if puntuacion < 1 or puntuacion > 10:
            return {
                "ok": False,
                "mensaje": "La puntuación debe estar entre 1 y 10"
            }

        pelicula.titulo = datos["titulo"]
        pelicula.director = datos["director"]
        pelicula.puntuacion = puntuacion

        session.commit()

        return {
            "ok": True,
            "mensaje": "🎉 Película actualizada correctamente"
        }

    except Exception as error:
        session.rollback()

        print("❌ Error actualizando película:")
        print(error)

        return {
            "ok": False,
            "mensaje": "Ocurrió un error al actualizar"
        }

    finally:
        session.close()


# [NUEVO]
def eliminar(id):
    session = Session()

    try:
        pelicula = (
            session.query(Pelicula)
            .filter(Pelicula.id == id)
            .first()
        )

        if not pelicula:
            return {
                "ok": False,
                "mensaje": "Película no encontrada"
            }

        session.delete(pelicula)

        session.commit()

        return {
            "ok": True,
            "mensaje": "🗑️ Película eliminada correctamente"
        }

    except Exception as error:
        session.rollback()

        print("❌ Error eliminando película:")
        print(error)

        return {
            "ok": False,
            "mensaje": "Ocurrió un error al eliminar"
        }

    finally:
        session.close()



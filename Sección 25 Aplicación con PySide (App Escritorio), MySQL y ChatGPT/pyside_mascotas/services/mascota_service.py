from database import Session
from models.mascota import Mascota


# =========================================================
# Obtener todas las mascotas
# =========================================================
def obtener_todos():

    session = Session()

    try:
        mascotas = session.query(Mascota).all()

        return mascotas

    finally:
        session.close()


# =========================================================
# Crear mascota
# =========================================================
# Guarda una nueva mascota en la base de datos
def crear(datos):

    session = Session()

    try:

        # =========================================================
        # Validaciones básicas
        # =========================================================
        if not datos["nombre"].strip():

            return {
                "ok": False,
                "mensaje": "El nombre es obligatorio"
            }

        if not datos["especie"].strip():

            return {
                "ok": False,
                "mensaje": "La especie es obligatoria"
            }

        if datos["peso"] <= 0:

            return {
                "ok": False,
                "mensaje": "El peso debe ser mayor a 0"
            }

        # =========================================================
        # Crear instancia ORM
        # =========================================================
        mascota = Mascota(
            nombre=datos["nombre"],
            especie=datos["especie"],
            peso=datos["peso"]
        )

        # Guardar en sesión
        session.add(mascota)

        # Confirmar cambios
        session.commit()

        return {
            "ok": True,
            "mensaje": "Mascota guardada correctamente"
        }

    except Exception as error:

        session.rollback()

        return {
            "ok": False,
            "mensaje": str(error)
        }

    finally:
        session.close()

# =========================================================
# Obtener mascota por ID
# =========================================================
def obtener_por_id(mascota_id):

    session = Session()

    try:

        mascota = (
            session.query(Mascota)
            .filter(Mascota.id == mascota_id)
            .first()
        )

        return mascota

    finally:
        session.close()



# =========================================================
# Actualizar mascota
# =========================================================
def actualizar(mascota_id, datos):

    session = Session()

    try:

        mascota = (
            session.query(Mascota)
            .filter(Mascota.id == mascota_id)
            .first()
        )

        # =========================================================
        # Validar existencia
        # =========================================================
        if not mascota:

            return {
                "ok": False,
                "mensaje": "Mascota no encontrada"
            }

        # =========================================================
        # Validaciones básicas
        # =========================================================
        if not datos["nombre"].strip():

            return {
                "ok": False,
                "mensaje": "El nombre es obligatorio"
            }

        if not datos["especie"].strip():

            return {
                "ok": False,
                "mensaje": "La especie es obligatoria"
            }

        if datos["peso"] <= 0:

            return {
                "ok": False,
                "mensaje": "El peso debe ser mayor a 0"
            }

        # =========================================================
        # Actualizar datos
        # =========================================================
        mascota.nombre = datos["nombre"]

        mascota.especie = datos["especie"]

        mascota.peso = datos["peso"]

        # =========================================================
        # Confirmar cambios
        # =========================================================
        session.commit()

        return {
            "ok": True,
            "mensaje": "Mascota actualizada correctamente"
        }

    except Exception as error:

        session.rollback()

        return {
            "ok": False,
            "mensaje": str(error)
        }

    finally:
        session.close()


# =========================================================
# Eliminar mascota
# =========================================================
def eliminar(mascota_id):

    session = Session()

    try:

        mascota = (
            session.query(Mascota)
            .filter(Mascota.id == mascota_id)
            .first()
        )

        # =========================================================
        # Validar existencia
        # =========================================================
        if not mascota:

            return {
                "ok": False,
                "mensaje": "Mascota no encontrada"
            }

        # =========================================================
        # Eliminar registro
        # =========================================================
        session.delete(mascota)

        # =========================================================
        # Confirmar cambios
        # =========================================================
        session.commit()

        return {
            "ok": True,
            "mensaje": "Mascota eliminada correctamente"
        }

    except Exception as error:

        session.rollback()

        return {
            "ok": False,
            "mensaje": str(error)
        }

    finally:
        session.close()
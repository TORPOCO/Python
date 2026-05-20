import axios from "axios";

export const urlBase = "http://localhost:8080/api/libros";

const librosAPI = axios.create({
  baseURL: urlBase,
});

// [EXISTENTE]
export async function listarLibros() {
  const respuesta = await librosAPI.get();
  return respuesta.data;
}

// [EXISTENTE]
export async function crearLibro(libro) {
  if (!libro.titulo || !libro.autor || !libro.rating) {
    throw new Error("Todos los campos son obligatorios");
  }

  if (libro.rating < 1 || libro.rating > 5) {
    throw new Error("El rating debe estar entre 1 y 5");
  }

  const respuesta = await librosAPI.post("", libro);
  return respuesta.data;
}

// [EXISTENTE]
export async function obtenerLibroPorId(id) {
  const respuesta = await librosAPI.get(`/${id}`);
  return respuesta.data;
}

// [EXISTENTE]
export async function actualizarLibro(id, libro) {
  if (!libro.titulo || !libro.autor || !libro.rating) {
    throw new Error("Todos los campos son obligatorios");
  }

  if (libro.rating < 1 || libro.rating > 5) {
    throw new Error("El rating debe estar entre 1 y 5");
  }

  const respuesta = await librosAPI.put(`/${id}`, libro);
  return respuesta.data;
}

// [NUEVO]
export async function eliminarLibro(id) {
  const respuesta = await librosAPI.delete(`/${id}`);
  return respuesta.data;
}

export default librosAPI;
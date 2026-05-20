import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import {
  listarLibros,
  eliminarLibro,
} from "../Api/libros";

function ListadoLibros() {
  const [libros, setLibros] = useState([]);

  // [EXISTENTE]
  useEffect(() => {
    cargarLibros();
  }, []);

  // [EXISTENTE]
  async function cargarLibros() {
    const datos = await listarLibros();
    setLibros(datos);
  }

  // [NUEVO]
  async function eliminar(id) {
    const confirmar = confirm(
      "¿Está seguro de eliminar este libro?"
    );

    if (!confirmar) {
      return;
    }

    try {
      await eliminarLibro(id);

      alert("Libro eliminado correctamente");

      cargarLibros();
    } catch (error) {
      alert("Error al eliminar el libro");
    }
  }

  return (
    <div className="container mt-4">
      <h2 className="text-warning text-center">
        <i className="bi bi-book-half me-2"></i>
        Listado de Libros
      </h2>

      <table className="table table-striped table-hover mt-4">
        <thead className="table-primary">
          <tr>
            <th>ID</th>
            <th>Título</th>
            <th>Autor</th>
            <th>Rating</th>
            <th>Acciones</th>
          </tr>
        </thead>

        <tbody>
          {libros.map((libro) => (
            <tr key={libro.id}>
              <td>{libro.id}</td>
              <td>{libro.titulo}</td>
              <td>{libro.autor}</td>
              <td>{libro.rating}</td>

              <td>
                <div className="d-flex gap-2">
                  <Link
                    className="btn btn-primary btn-sm"
                    to={`/editar/${libro.id}`}
                  >
                    <i className="bi bi-pencil-square me-2"></i>
                    Editar
                  </Link>

                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => eliminar(libro.id)}
                  >
                    <i className="bi bi-trash me-2"></i>
                    Eliminar
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ListadoLibros;
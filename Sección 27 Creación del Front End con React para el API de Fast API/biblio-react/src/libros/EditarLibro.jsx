import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import {
  obtenerLibroPorId,
  actualizarLibro,
} from "../Api/libros";

function EditarLibro() {
  const navigate = useNavigate();

  const { id } = useParams();

  const [titulo, setTitulo] = useState("");
  const [autor, setAutor] = useState("");
  const [rating, setRating] = useState("");

  // [EXISTENTE]
  useEffect(() => {
    cargarLibro();
  }, []);

  // [EXISTENTE]
  async function cargarLibro() {
    const libro = await obtenerLibroPorId(id);

    setTitulo(libro.titulo);
    setAutor(libro.autor);
    setRating(libro.rating);
  }

  // [NUEVO]
  async function guardarCambios(e) {
    e.preventDefault();

    try {
      const libro = {
        titulo,
        autor,
        rating: parseInt(rating),
      };

      await actualizarLibro(id, libro);

      alert("Libro actualizado correctamente");

      navigate("/");
    } catch (error) {
      alert(error.message);
    }
  }

  return (
    <div className="container mt-4">
      <h2 className="text-warning text-center">
        <i className="bi bi-book-half me-2"></i>
        Editar Libro
      </h2>

      <form className="mt-4" onSubmit={guardarCambios}>
        <div className="mb-3">
          <label className="form-label">Título</label>

          <input
            type="text"
            className="form-control"
            placeholder="Ingrese el título"
            value={titulo}
            onChange={(e) => setTitulo(e.target.value)}
          />
        </div>

        <div className="mb-3">
          <label className="form-label">Autor</label>

          <input
            type="text"
            className="form-control"
            placeholder="Ingrese el autor"
            value={autor}
            onChange={(e) => setAutor(e.target.value)}
          />
        </div>

        <div className="mb-3">
          <label className="form-label">Rating</label>

          <input
            type="number"
            className="form-control"
            placeholder="Ingrese el rating"
            min="1"
            max="5"
            value={rating}
            onChange={(e) => setRating(e.target.value)}
          />
        </div>

        <div className="d-flex gap-2">
          <button type="submit" className="btn btn-primary">
            <i className="bi bi-save me-2"></i>
            Guardar Cambios
          </button>

          <button
            type="button"
            className="btn btn-secondary"
            onClick={() => navigate("/")}
          >
            <i className="bi bi-x-circle me-2"></i>
            Cancelar
          </button>
        </div>
      </form>
    </div>
  );
}

export default EditarLibro;
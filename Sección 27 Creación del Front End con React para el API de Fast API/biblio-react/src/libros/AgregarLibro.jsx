import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { crearLibro } from "../Api/libros";

function AgregarLibro() {
  const navigate = useNavigate();

  const [titulo, setTitulo] = useState("");
  const [autor, setAutor] = useState("");
  const [rating, setRating] = useState("");

  // [NUEVO]
  async function guardarLibro(e) {
    e.preventDefault();

    try {
      const libro = {
        titulo,
        autor,
        rating: parseInt(rating),
      };

      await crearLibro(libro);

      alert("Libro agregado correctamente");

      navigate("/");
    } catch (error) {
      alert(error.message);
    }
  }

  return (
    <div className="container mt-4">
      <h2 className="text-warning text-center">
        <i className="bi bi-book-half me-2"></i>
        Agregar Libro
      </h2>

      <form className="mt-4" onSubmit={guardarLibro}>
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
          <button type="submit" className="btn btn-success">
            <i className="bi bi-check-circle me-2"></i>
            Guardar
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

export default AgregarLibro;
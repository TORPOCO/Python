import { Link } from "react-router-dom";

function Navegacion() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
      <div className="container">
        <Link className="navbar-brand" to="/">
          <i className="bi bi-book-half me-2"></i>
          Biblioteca Personal
        </Link>

        <div>
          <Link className="btn btn-success" to="/agregar">
            <i className="bi bi-plus-circle me-2"></i>
            Agregar Libro
          </Link>
        </div>
      </div>
    </nav>
  );
}

export default Navegacion;
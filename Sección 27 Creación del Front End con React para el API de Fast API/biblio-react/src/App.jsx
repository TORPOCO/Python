import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navegacion from "./componentes/Navegacion";
import ListadoLibros from "./libros/ListadoLibros";
import AgregarLibro from "./libros/AgregarLibro";
import EditarLibro from "./libros/EditarLibro";

function App() {
  return (
    <BrowserRouter>
      <Navegacion />

      <Routes>
        <Route path="/" element={<ListadoLibros />} />

        <Route path="/agregar" element={<AgregarLibro />} />

        <Route path="/editar/:id" element={<EditarLibro />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
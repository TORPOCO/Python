import sys
import os
os.environ["QT_API"] = "pyside6"

import qdarkstyle

from PySide6.QtCore import Qt

from PySide6.QtGui import QAction

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QToolBar,
)

from views.form_view import FormView
from views.home_view import HomeView


# =========================================================
# Ventana principal
# =========================================================
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # =========================================================
        # Configuración ventana
        # =========================================================
        self.setWindowTitle("🐾 PySide Mascotas")

        self.resize(1280, 720)

        # =========================================================
        # Stack de navegación
        # =========================================================
        self.stack = QStackedWidget()

        self.setCentralWidget(self.stack)

        # =========================================================
        # Crear vistas
        # =========================================================
        self.home_view = HomeView(
            editar_callback=self.editar_mascota
        )

        # [MODIFICADO]
        self.form_view = FormView(
            volver_inicio=self.mostrar_inicio,
            refrescar_home=self.home_view.cargar_datos
        )

        # =========================================================
        # Agregar vistas al stack
        # =========================================================
        self.stack.addWidget(self.home_view)

        self.stack.addWidget(self.form_view)

        # =========================================================
        # Toolbar principal
        # =========================================================
        toolbar = QToolBar("Navegación")

        toolbar.setMovable(False)

        self.addToolBar(
            Qt.TopToolBarArea,
            toolbar
        )

        # =========================================================
        # Acción inicio
        # =========================================================
        action_inicio = QAction(
            "🏠 Inicio",
            self
        )

        action_inicio.triggered.connect(
            self.mostrar_inicio
        )

        toolbar.addAction(action_inicio)

        # =========================================================
        # Acción agregar mascota
        # =========================================================
        action_agregar = QAction(
            "➕ Agregar Mascota",
            self
        )

        action_agregar.triggered.connect(
            self.mostrar_formulario
        )

        toolbar.addAction(action_agregar)

        # =========================================================
        # Mostrar inicio por defecto
        # =========================================================
        self.mostrar_inicio()

    # =========================================================
    # Mostrar pantalla inicio
    # =========================================================
    def mostrar_inicio(self):

        self.stack.setCurrentWidget(
            self.home_view
        )

    # =========================================================
    # Mostrar formulario
    # =========================================================
    def mostrar_formulario(self):

        self.stack.setCurrentWidget(
            self.form_view
        )

    # [MODIFICADO]
    def editar_mascota(self, mascota_id):
        # =========================================================
        # Cargar mascota en formulario
        # =========================================================
        self.form_view.cargar_mascota(
            mascota_id
        )

        # =========================================================
        # Mostrar formulario
        # =========================================================
        self.mostrar_formulario()

# =========================================================
# Punto entrada aplicación
# =========================================================
def main():

    app = QApplication(sys.argv)

    # Tema oscuro global
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    # Crear ventana
    window = MainWindow()

    # Mostrar ventana
    window.show()

    # Ejecutar aplicación
    sys.exit(app.exec())


# Ejecutar aplicación
if __name__ == "__main__":
    main()
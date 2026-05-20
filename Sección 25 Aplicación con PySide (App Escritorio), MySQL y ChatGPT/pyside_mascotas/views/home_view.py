from PySide6.QtCore import Qt

from PySide6.QtGui import QStandardItem
from PySide6.QtGui import QStandardItemModel

from PySide6.QtWidgets import (
    QLabel,
    QSizePolicy,
    QTableView,
    QVBoxLayout,
    QWidget,
    QHeaderView,
    QMessageBox,
)

from services.mascota_service import obtener_todos


# =========================================================
# Vista principal
# =========================================================
class HomeView(QWidget):

    # Modificar constructor
    def __init__(self, editar_callback=None):
        super().__init__()

        # =========================================================
        # Guardar callback
        # =========================================================
        self.editar_callback = editar_callback


        # =========================================================
        # Layout principal
        # =========================================================
        layout = QVBoxLayout()

        layout.setContentsMargins(40, 30, 40, 30)

        layout.setSpacing(15)

        layout.setAlignment(Qt.AlignTop)

        self.setLayout(layout)

        # =========================================================
        # Título principal
        # =========================================================
        titulo = QLabel("🐾 PySide Mascotas")

        titulo.setAlignment(Qt.AlignCenter)

        titulo.setStyleSheet("""
            font-size: 20pt;
            font-weight: bold;
        """)

        titulo.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred
        )

        # =========================================================
        # Subtítulo
        # =========================================================
        subtitulo = QLabel(
            "Sistema de Adopción de Mascotas"
        )

        subtitulo.setAlignment(Qt.AlignCenter)

        subtitulo.setStyleSheet("""
            font-size: 11pt;
        """)

        subtitulo.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred
        )

        # =========================================================
        # Tabla mascotas
        # =========================================================
        self.table = QTableView()

        self.table.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        self.table.verticalHeader().setVisible(False)

        self.table.setSelectionBehavior(
            QTableView.SelectRows
        )

        self.table.setEditTriggers(
            QTableView.NoEditTriggers
        )

        self.table.setVerticalScrollBarPolicy(
            Qt.ScrollBarAsNeeded
        )

        self.table.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        self.table.verticalHeader().setDefaultSectionSize(38)

        self.table.setStyleSheet("""
            QTableView {
                border: none;
            }
        """)

        # =========================================================
        # Modelo tabla
        # =========================================================
        self.model = QStandardItemModel()

        self.model.setHorizontalHeaderLabels([
            "ID",
            "Nombre",
            "Especie",
            "Peso (kg)"
        ])

        # =========================================================
        # Cargar datos iniciales
        # =========================================================
        self.cargar_datos()

        self.table.setModel(self.model)

        # =========================================================
        # Detectar doble clic en filas
        # =========================================================
        self.table.doubleClicked.connect(
            self.editar_mascota
        )

        # =========================================================
        # Configuración columnas responsive
        # =========================================================
        header = self.table.horizontalHeader()

        for i in range(self.model.columnCount()):
            header.setSectionResizeMode(
                i,
                QHeaderView.Stretch
            )

        # =========================================================
        # Contenedor tabla
        # =========================================================
        table_container = QWidget()

        table_layout = QVBoxLayout()

        table_layout.setContentsMargins(
            120,
            0,
            120,
            0
        )

        table_layout.setAlignment(Qt.AlignTop)

        table_container.setLayout(table_layout)

        table_layout.addWidget(self.table)

        # =========================================================
        # Agregar widgets al layout
        # =========================================================
        layout.addWidget(titulo)

        layout.addWidget(subtitulo)

        layout.addWidget(table_container)


    # =========================================================
    # Cargar datos en tabla
    # =========================================================
    def cargar_datos(self):
        # Limpiar filas actuales
        self.model.setRowCount(0)

        mascotas = obtener_todos()

        for mascota in mascotas:
            fila = [
            QStandardItem(str(mascota.id)),
            QStandardItem(mascota.nombre),
            QStandardItem(mascota.especie),
            QStandardItem(str(mascota.peso)),
            ]

            self.model.appendRow(fila)

    # =========================================================
    # Editar mascota
    # =========================================================
    def editar_mascota(self, index):

        # Obtener fila seleccionada
        fila = index.row()

        # Obtener ID desde columna 0
        mascota_id = int(
            self.model.item(fila, 0).text()
        )

        # =========================================================
        # Mostrar confirmación visual temporal
        # =========================================================
        QMessageBox.information(
            self,
            "Editar",
            f"Se editará la mascota ID: {mascota_id}"
        )

        # =========================================================
        # Ejecutar callback edición
        # =========================================================
        if self.editar_callback:
            self.editar_callback(mascota_id)
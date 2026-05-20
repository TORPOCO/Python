from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QDoubleSpinBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
    QMessageBox,
)

# Actualizar import del service
from services.mascota_service import (
    actualizar,
    crear,
    eliminar,
    obtener_por_id
)

# =========================================================
# Vista formulario mascotas
# =========================================================
class FormView(QWidget):

    # Modificar constructor
    def __init__(self,volver_inicio=None,refrescar_home=None):
        super().__init__()

        # =========================================================
        # Mascota en edición
        # =========================================================
        self.mascota_id = None

        self.volver_inicio = volver_inicio

        # Guardar callback nuevo
        self.refrescar_home = refrescar_home

        # =========================================================
        # Layout principal
        # =========================================================
        layout = QVBoxLayout()

        layout.setContentsMargins(40, 30, 40, 30)

        layout.setSpacing(20)

        layout.setAlignment(Qt.AlignTop)

        self.setLayout(layout)

        # =========================================================
        # Título formulario
        # =========================================================
        # [MODIFICADO]
        self.titulo = QLabel("➕ Agregar Mascota")

        # [MODIFICADO]
        self.titulo.setAlignment(Qt.AlignCenter)

        # [MODIFICADO]
        self.titulo.setStyleSheet("""
            font-size: 20pt;
            font-weight: bold;
        """)

        # [MODIFICADO]
        self.titulo.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred
        )

        # =========================================================
        # Subtítulo
        # =========================================================
        subtitulo = QLabel(
            "Formulario de registro de mascotas"
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
        # Contenedor formulario
        # =========================================================
        form_container = QWidget()

        form_container.setMaximumWidth(500)

        form_layout_container = QVBoxLayout()

        form_layout_container.setAlignment(
            Qt.AlignTop
        )

        form_container.setLayout(
            form_layout_container
        )

        # =========================================================
        # Formulario
        # =========================================================
        # mostrar formulario vacío
        form_layout = QFormLayout()

        form_layout.setLabelAlignment(
            Qt.AlignLeft
        )

        form_layout.setFormAlignment(
            Qt.AlignTop
        )

        form_layout.setVerticalSpacing(15)

        # =========================================================
        # Campo nombre
        # =========================================================
        self.input_nombre = QLineEdit()

        self.input_nombre.setPlaceholderText(
            "Ingrese el nombre"
        )

        # =========================================================
        # Campo especie
        # =========================================================
        self.input_especie = QLineEdit()

        self.input_especie.setPlaceholderText(
            "Ingrese la especie"
        )

        # =========================================================
        # Campo peso
        # =========================================================
        self.input_peso = QDoubleSpinBox()

        self.input_peso.setRange(0, 999)

        self.input_peso.setDecimals(2)

        self.input_peso.setSuffix(" kg")

        # =========================================================
        # Agregar campos formulario
        # =========================================================
        form_layout.addRow(
            "Nombre:",
            self.input_nombre
        )

        form_layout.addRow(
            "Especie:",
            self.input_especie
        )

        form_layout.addRow(
            "Peso:",
            self.input_peso
        )

        # =========================================================
        # Contenedor botones
        # =========================================================
        botones_layout = QHBoxLayout()

        botones_layout.setSpacing(10)

        # =========================================================
        # Botón guardar
        # =========================================================
        # [MODIFICADO]
        self.btn_guardar = QPushButton(
            "💾 Guardar"
        )

        # Conectar botón guardar
        self.btn_guardar.clicked.connect(
            self.guardar_mascota
        )

        # =========================================================
        # Botón cancelar
        # =========================================================
        btn_cancelar = QPushButton(
            "❌ Cancelar"
        )

        # =========================================================
        # Botón eliminar
        # =========================================================
        self.btn_eliminar = QPushButton(
            "🗑️ Eliminar"
        )

        # Oculto inicialmente
        self.btn_eliminar.hide()

        self.btn_eliminar.clicked.connect(
            self.eliminar_mascota
        )


        # Volver a inicio
        if self.volver_inicio:
            btn_cancelar.clicked.connect(
                self.volver_inicio
            )

        # =========================================================
        # Agregar botones
        # =========================================================
        # [MODIFICADO]
        botones_layout.addWidget(self.btn_guardar)

        botones_layout.addWidget(
            self.btn_eliminar
        )

        botones_layout.addWidget(btn_cancelar)

        # =========================================================
        # Agregar formulario al contenedor
        # =========================================================
        form_layout_container.addLayout(
            form_layout
        )

        form_layout_container.addLayout(
            botones_layout
        )

        # =========================================================
        # Contenedor centrado
        # =========================================================
        center_container = QWidget()

        center_layout = QVBoxLayout()

        center_layout.setAlignment(Qt.AlignTop)

        center_layout.addWidget(
            form_container,
            alignment=Qt.AlignHCenter
        )

        center_container.setLayout(center_layout)

        # =========================================================
        # Agregar widgets principales
        # =========================================================
        layout.addWidget(self.titulo)

        layout.addWidget(subtitulo)

        layout.addWidget(center_container)

    # =========================================================
    # Guardar mascota
    # =========================================================
    # procesar y actualizar
    def guardar_mascota(self):

        datos = {
            "nombre": self.input_nombre.text(),
            "especie": self.input_especie.text(),
            "peso": self.input_peso.value(),
        }

        # =========================================================
        # Modo edición
        # =========================================================
        if self.mascota_id:

            resultado = actualizar(
                self.mascota_id,
                datos
            )

        # =========================================================
        # Modo creación
        # =========================================================
        else:

            resultado = crear(datos)

        # =========================================================
        # Error validación
        # =========================================================
        if not resultado["ok"]:
            QMessageBox.warning(
                self,
                "Error",
                resultado["mensaje"]
            )

            return

        # =========================================================
        # Mensaje éxito
        # =========================================================
        QMessageBox.information(
            self,
            "Éxito",
            resultado["mensaje"]
        )

        # =========================================================
        # Limpiar formulario
        # =========================================================
        self.input_nombre.clear()

        self.input_especie.clear()

        self.input_peso.setValue(0)

        # =========================================================
        # Restaurar modo creación
        # =========================================================
        self.mascota_id = None

        self.titulo.setText(
            "➕ Agregar Mascota"
        )

        self.btn_guardar.setText(
            "💾 Guardar"
        )

        # Ocultar botón eliminar al restaurar modo creación
        self.btn_eliminar.hide()

        # =========================================================
        # Refrescar tabla principal
        # =========================================================
        if self.refrescar_home:
            self.refrescar_home()

        # =========================================================
        # Volver a inicio
        # =========================================================
        if self.volver_inicio:
            self.volver_inicio()

    # =========================================================
    # Eliminar mascota
    # =========================================================
    def eliminar_mascota(self):

        # =========================================================
        # Validar ID
        # =========================================================
        if not self.mascota_id:
            return

        # =========================================================
        # Confirmación simple
        # =========================================================
        respuesta = QMessageBox.question(
            self,
            "Confirmar",
            "¿Desea eliminar esta mascota?"
        )

        # =========================================================
        # Cancelar eliminación
        # =========================================================
        if respuesta != QMessageBox.Yes:
            return

        # =========================================================
        # Eliminar registro
        # =========================================================
        resultado = eliminar(
            self.mascota_id
        )

        # =========================================================
        # Mostrar error
        # =========================================================
        if not resultado["ok"]:
            QMessageBox.warning(
                self,
                "Error",
                resultado["mensaje"]
            )

            return

        # =========================================================
        # Mensaje éxito
        # =========================================================
        QMessageBox.information(
            self,
            "Éxito",
            resultado["mensaje"]
        )

        # =========================================================
        # Limpiar formulario
        # =========================================================
        self.input_nombre.clear()

        self.input_especie.clear()

        self.input_peso.setValue(0)

        # =========================================================
        # Restaurar modo creación
        # =========================================================
        self.mascota_id = None

        self.titulo.setText(
            "➕ Agregar Mascota"
        )

        self.btn_guardar.setText(
            "💾 Guardar"
        )

        self.btn_eliminar.hide()

        # =========================================================
        # Refrescar listado
        # =========================================================
        if self.refrescar_home:
            self.refrescar_home()

        # =========================================================
        # Volver al inicio
        # =========================================================
        if self.volver_inicio:
            self.volver_inicio()



    # =========================================================
    # Cargar mascota para edición
    # =========================================================
    # cargar y mostrar formulario con datos
    def cargar_mascota(self, mascota_id):

        mascota = obtener_por_id(mascota_id)

        if not mascota:
            return

        # =========================================================
        # Guardar ID actual
        # =========================================================
        self.mascota_id = mascota.id

        # =========================================================
        # Actualizar encabezado
        # =========================================================
        self.titulo.setText(
            "✏️ Editar Mascota"
        )

        # =========================================================
        # Actualizar botón
        # =========================================================
        self.btn_guardar.setText(
            "💾 Guardar Cambios"
        )
        # Mostrar botón eliminar en edición
        self.btn_eliminar.show()

        # =========================================================
        # Precargar datos
        # =========================================================
        self.input_nombre.setText(
            mascota.nombre
        )

        self.input_especie.setText(
            mascota.especie
        )

        self.input_peso.setValue(
            mascota.peso
        )
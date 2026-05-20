import flet as ft

# [MODIFICADO]
from services.pelicula_service import (
    obtener_todos,
    eliminar
)
# [NUEVO]
from components.dialogs import confirmar_eliminacion


# [MODIFICADO]
def home_view(page: ft.Page):
    # [NUEVO]

    peliculas = obtener_todos()

    filas = []

    async def eliminar_pelicula(pelicula_id):
        resultado = eliminar(pelicula_id)

        page.snack_bar = ft.SnackBar(
            content=ft.Text(resultado["mensaje"]),
            bgcolor=(
                ft.Colors.GREEN_400
                if resultado["ok"]
                else ft.Colors.RED_400
            )
        )
        page.snack_bar.open = True
        page.update()

    # [NUEVO]
    def abrir_dialogo(pelicula_id):
        dialogo = confirmar_eliminacion(
            page,
            lambda: eliminar_pelicula(pelicula_id)
        )
        # Importante:
        # insertar el diálogo en page.overlay antes de abrirlo
        page.overlay.append(dialogo)
        dialogo.open = True
        page.update()

    for pelicula in peliculas:
        filas.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(pelicula.id))),
                    ft.DataCell(ft.Text(pelicula.titulo)),
                    ft.DataCell(ft.Text(pelicula.director)),
                    ft.DataCell(ft.Text(str(pelicula.puntuacion))),
                    ft.DataCell(
                        ft.Row(
                            controls=[
                                # [MODIFICADO]
                                ft.IconButton(
                                    icon=ft.Icons.EDIT,
                                    icon_color=ft.Colors.AMBER_400,
                                    tooltip="Editar",
                                    on_click=lambda e, pelicula_id=pelicula.id:
                                    page.go(f"/editar/{pelicula_id}")
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    icon_color=ft.Colors.RED_400,
                                    tooltip="Eliminar",
                                    on_click=lambda e, pelicula_id=pelicula.id: abrir_dialogo(
                                        pelicula_id
                                    )
                                ),
                            ]
                        )
                    ),
                ]
            )
        )

    tabla = ft.DataTable(

        bgcolor=ft.Colors.BLUE_GREY_800,
        border_radius=10,
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Título")),
            ft.DataColumn(ft.Text("Director")),
            ft.DataColumn(ft.Text("Puntuación")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=filas,
    )

    return ft.Container(
        padding=30,

        content=ft.Column(

            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(
                    ft.Icons.MOVIE,
                    size=80,
                    color=ft.Colors.AMBER_400,
                ),
                ft.Text(
                    "Sistema de Películas",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Listado general de películas",
                    size=16,
                    color=ft.Colors.WHITE70,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(

                    width=1000,
                    padding=20,
                    content=ft.Column(

                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Row(

                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    tabla
                                ]
                            )
                        ]
                    )
                )
            ],
        ),
    )

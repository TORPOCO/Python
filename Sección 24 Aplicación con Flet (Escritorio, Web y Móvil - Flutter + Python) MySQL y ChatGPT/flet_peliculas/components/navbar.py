import flet as ft


def navbar(page: ft.Page):
    return ft.Container(
        padding=15,
        bgcolor=ft.Colors.BLUE_GREY_800,
        border_radius=10,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.ElevatedButton(
                    "Inicio",
                    icon=ft.Icons.HOME,
                    on_click=lambda e: page.go("/")
                ),
                ft.ElevatedButton(
                    "Agregar Película",
                    icon=ft.Icons.ADD,
                    on_click=lambda e: page.go("/agregar")
                ),
            ]
        )
    )
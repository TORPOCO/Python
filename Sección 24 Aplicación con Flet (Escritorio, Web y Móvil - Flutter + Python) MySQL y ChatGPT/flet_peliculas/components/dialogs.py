import flet as ft
import asyncio   # ✅ agregar esto


def confirmar_eliminacion(page, on_confirmar):
    dialogo = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirmar eliminación"),
        content=ft.Text(
            "¿Seguro que deseas eliminar esta película?"
        ),
        actions=[
            ft.TextButton(
                "Cancelar",
                on_click=lambda e: cerrar_dialogo(page, dialogo)
            ),
            ft.TextButton(
                "Eliminar",
                on_click=lambda e: confirmar(
                    e,
                    page,
                    dialogo,
                    on_confirmar
                )
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    return dialogo


def cerrar_dialogo(page, dialogo):
    dialogo.open = False
    page.update()


def confirmar(e, page, dialogo, on_confirmar):
    dialogo.open = False

    # ✅ FIX IMPORTANTE
    asyncio.create_task(on_confirmar())
    page.update()
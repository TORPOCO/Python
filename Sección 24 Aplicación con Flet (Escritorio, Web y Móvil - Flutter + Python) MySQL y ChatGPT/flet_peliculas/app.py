import flet as ft

from components.navbar import navbar
from views.home_view import home_view
from views.form_view import form_view

async def main(page: ft.Page):
    page.title = "🎞️ Flet Películas"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900

    vertical_alignment = ft.MainAxisAlignment.CENTER,
    # [NUEVO]
    def cambiar_ruta(route):
        page.views.clear()

        # [NUEVO]
        if page.route == "/":
            page.views.append(
                ft.View(
                    route="/",
                    bgcolor=ft.Colors.BLUE_GREY_900,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        navbar(page),
                        # [MODIFICADO]
                        home_view(page),
                    ],
                )
            )

        # [NUEVO]
        elif page.route == "/agregar":
            page.views.append(
                ft.View(
                    route="/agregar",
                    bgcolor=ft.Colors.BLUE_GREY_900,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        navbar(page),
                        form_view(page),
                    ],
                )
            )
        # [MODIFICADO]
        elif page.route.startswith("/editar/"):
            pelicula_id = page.route.split("/")[-1]
            page.views.append(
                ft.View(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    route=page.route,
                    bgcolor=ft.Colors.BLUE_GREY_900,
                    controls=[
                        navbar(page),
                        form_view(page, pelicula_id),
                    ],
                )
            )

        page.update()




    # [NUEVO]
    page.on_route_change = cambiar_ruta

    # [NUEVO]
    page.go("/")

    # RENDER MANUAL
    cambiar_ruta("/")


if __name__ == "__main__":
    ft.run(main)
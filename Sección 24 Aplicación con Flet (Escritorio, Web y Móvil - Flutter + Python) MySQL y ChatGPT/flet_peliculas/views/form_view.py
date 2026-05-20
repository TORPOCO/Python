import flet as ft
# [MODIFICADO]
from services.pelicula_service import (
    crear,
    obtener_por_id,
    actualizar
)


# [MODIFICADO]
def form_view(page: ft.Page, pelicula_id=None):
    # GET: mostrar formulario vacío

    # [NUEVO]
    pelicula = None

    # GET: cargar y mostrar formulario con datos
    if pelicula_id:
        pelicula = obtener_por_id(int(pelicula_id))

    # [NUEVO]
    boton_guardar = ft.ElevatedButton(
        "Guardar cambios" if pelicula else "Guardar",
        icon=ft.Icons.SAVE,
        disabled=True,
    )


    # [NUEVO]
    def validar_formulario(e=None):
        # [NUEVO]
        boton_guardar.on_click = guardar_pelicula
        titulo = campo_titulo.value.strip()
        director = campo_director.value.strip()
        puntuacion = campo_puntuacion.value.strip()

        error_puntuacion = None

        if puntuacion:

            try:
                numero = int(puntuacion)

                if numero < 1 or numero > 10:
                    error_puntuacion = (
                        "Debe estar entre 1 y 10"
                    )

            except ValueError:
                error_puntuacion = (
                    "Debe ser un número entero"
                )

        campo_puntuacion.error_text = error_puntuacion

        formulario_valido = (
            titulo != ""
            and director != ""
            and puntuacion != ""
            and error_puntuacion is None
        )

        boton_guardar.disabled = not formulario_valido

        page.update()



    # [NUEVO]
    def guardar_pelicula(e):

        # POST: procesar y guardar
        datos = {
            "titulo": campo_titulo.value,
            "director": campo_director.value,
            "puntuacion": campo_puntuacion.value,
        }

        # [MODIFICADO]
        if pelicula:
            # POST: procesar y actualizar
            resultado = actualizar(
                pelicula.id,
                datos
            )

        else:
            # POST: procesar y guardar
            resultado = crear(datos)

        page.snack_bar = ft.SnackBar(
            content=ft.Text(resultado["mensaje"]),
            # [MODIFICADO]
            bgcolor=(
                ft.Colors.GREEN_500
                if resultado["ok"]
                # [MODIFICADO]
                else ft.Colors.RED_500
            )
        )

        page.snack_bar.open = True

        page.update()

        if resultado["ok"]:
            page.go("/")



    campo_titulo = ft.TextField(
        # [NUEVO]
        on_change=validar_formulario,
        value=pelicula.titulo if pelicula else "",
        label="Título",
        hint_text="Ingrese el título de la película",
        prefix_icon=ft.Icons.MOVIE,
        expand=True,
    )

    campo_director = ft.TextField(
        # [NUEVO]
        on_change=validar_formulario,
        value=pelicula.director if pelicula else "",
        label="Director",
        hint_text="Ingrese el director",
        prefix_icon=ft.Icons.PERSON,
        expand=True,
    )

    campo_puntuacion = ft.TextField(
        # [NUEVO]
        on_change=validar_formulario,
        value=str(pelicula.puntuacion) if pelicula else "",
        label="Puntuación",
        hint_text="Valor entre 1 y 10",
        prefix_icon=ft.Icons.STAR,
        keyboard_type=ft.KeyboardType.NUMBER,
        expand=True,
    )
    # [NUEVO]
    validar_formulario()
    return ft.Container(
        padding=30,
        content=ft.Column(
            tight=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(
                    ft.Icons.ADD_BOX,
                    size=80,
                    color=ft.Colors.AMBER_400,
                ),
                ft.Text(
                    # [MODIFICADO]
                    "Editar Película" if pelicula else "Agregar Película",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    # [MODIFICADO]
                    (
                        "Modifique los datos de la película"
                        if pelicula
                        else "Complete el formulario"
                    ),
                    size=16,
                    color=ft.Colors.WHITE70,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(
                    width=500,
                    padding=30,
                    bgcolor=ft.Colors.BLUE_GREY_800,
                    border_radius=15,
                    content=ft.Column(
                        tight=True,
                        spacing=20,
                        controls=[
                            campo_titulo,
                            campo_director,
                            campo_puntuacion,
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    # [MODIFICADO]
                                    boton_guardar,
                                    ft.OutlinedButton(
                                        "Cancelar",
                                        icon=ft.Icons.CANCEL,
                                        on_click=lambda e: page.go("/")
                                    ),
                                ]
                            )
                        ]
                    )
                )
            ]
        )
    )

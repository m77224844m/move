import flet as ft

def ClientsPage(page: ft.Page):
    return ft.View(
        route="/clients",
        appbar=ft.AppBar(title=ft.Text("العملاء")),
        controls=[
            ft.ElevatedButton("رجوع", on_click=lambda _: page.go("/home")),
        ]
    )
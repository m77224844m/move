import flet as ft

def AccountsPage(page: ft.Page):
    return ft.View(
        route="/accounts",
        appbar=ft.AppBar(title=ft.Text("الحسابات")),
        controls=[
            ft.ElevatedButton("رجوع", on_click=lambda _: page.go("/home")),
        ]
    )
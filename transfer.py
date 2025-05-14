import flet as ft

def TransferPage(page: ft.Page):
    return ft.View(
        route="/transfer",
        appbar=ft.AppBar(title=ft.Text("التحويل")),
        controls=[
            ft.ElevatedButton("رجوع", on_click=lambda _: page.go("/home")),
        ]
    )
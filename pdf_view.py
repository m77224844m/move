import flet as ft

def PdfViewPage(page: ft.Page):
    return ft.View(
        route="/pdf",
        appbar=ft.AppBar(title=ft.Text("عرض PDF")),
        controls=[
            ft.ElevatedButton("رجوع", on_click=lambda _: page.go("/home")),
        ]
    )
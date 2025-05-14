import flet as ft

def DailyCollectionPage(page: ft.Page):
    return ft.View(
        route="/daily",
        appbar=ft.AppBar(title=ft.Text("التحصيل اليومي")),
        controls=[
            ft.ElevatedButton("رجوع", on_click=lambda _: page.go("/home")),
        ]
    )
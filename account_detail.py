import flet as ft

def AccountDetailPage(page: ft.Page):
    return ft.View(
        route="/account_detail",
        appbar=ft.AppBar(title=ft.Text("تفاصيل الحساب")),
        controls=[
            ft.ElevatedButton("رجوع", on_click=lambda _: page.go("/home")),
        ]
    )
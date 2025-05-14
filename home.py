import flet as ft

def HomePage(page: ft.Page):
    return ft.View(
        route="/home",
        appbar=ft.AppBar(title=ft.Text("الرئيسية")),
        controls=[
            ft.ElevatedButton("العملاء", on_click=lambda _: page.go("/clients")),
            ft.ElevatedButton("الحسابات", on_click=lambda _: page.go("/accounts")),
            ft.ElevatedButton("التحصيل اليومي", on_click=lambda _: page.go("/daily")),
            ft.ElevatedButton("التحويل", on_click=lambda _: page.go("/transfer")),
            ft.ElevatedButton("تفاصيل الحساب", on_click=lambda _: page.go("/account_detail")),
            ft.ElevatedButton("عرض PDF", on_click=lambda _: page.go("/pdf")),
            ft.ElevatedButton("تسجيل الخروج", on_click=lambda _: page.go("/")),
        ]
    )
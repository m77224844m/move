import flet as ft
from login import login_page
from home import HomePage
from clients import ClientsPage
from accounts import AccountsPage
from account_detail import AccountDetailPage
from daily_collection import DailyCollectionPage

def main(page: ft.Page):
    page.title = "تطبيق بصفحتين"
    page.theme_mode = "light"
    # page.window_width = 400
    # page.window_height = 300
    page.padding = 20
    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "Escape" and len(page.views) > 1:
            page.views.pop()
            page.go(page.views[-1].route)

    page.on_keyboard_event = on_keyboard

    def route_change(e):
        page.views.clear()
        view = page.route
   
        if page.route == "/":
            page.views.append(login_page(page))
        elif page.route == "/home":
            page.views.append(HomePage(page))
        elif page.route == "/accounts":
            page.views.append(AccountsPage(page))
        elif page.route == "/clients":
            page.views.append(ClientsPage(page))
        elif page.route == "/account_detail":
            page.views.append(AccountDetailPage(page))
        elif page.route == "/daily_collection":
            page.views.append(DailyCollectionPage(page))
        # if view:
        #     page.views.append(view)
        #     page.update()



        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)

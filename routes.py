from flet import Page
from login import login_page
# from home import home_page
# from clients import clients_page
# from accounts import accounts_page
# from daily_collection import daily_collection_page
# from transfer import transfer_page
# from account_detail import account_detail_page
# from pdf_view import pdf_view_page

def route_handler(page: Page):
    route = page.route
    views = page.views

    # تنظيف كل العروض السابقة
    if route == "/":
        views.append(login_page(page))
    # elif route == "/home":
    #     views.append(home_page(page))
    # elif route == "/clients":
    #     views.append(clients_page(page))
    # elif route == "/accounts":
    #     views.append(accounts_page(page))
    # elif route == "/daily":
    #     views.append(daily_collection_page(page))
    # elif route == "/transfer":
    #     views.append(transfer_page(page))
    # elif route == "/account_detail":
    #     views.append(account_detail_page(page))
    # elif route == "/pdf":
    #     views.append(pdf_view_page(page))

    page.update()

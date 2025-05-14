from flet import *

def login_page(page: Page):
    username = TextField(label="اسم المستخدم", autofocus=True)
    password = TextField(label="كلمة المرور", password=True, can_reveal_password=True)
    message = Text(value="", color="red")

    def on_login_click(e):
        if username.value == "admin" and password.value == "123":
            message.value = ""
            page.go("/home")
        else:
            message.value = "❌ اسم المستخدم أو كلمة المرور غير صحيحة"
        page.update()

    return View(
        route="/",
        controls=[
            AppBar(title=Text("تسجيل الدخول"), bgcolor="blue"),
            Column(
                [
                    username,
                    password,
                    ElevatedButton(text="تسجيل الدخول", on_click=on_login_click),
                    message
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
            )
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER
    )

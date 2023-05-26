from django.urls import path
from .views import LoginCustom, LogoutCustom, changePassword


app_name = "auth"

urlpatterns = [
    path("login/", LoginCustom.as_view(template_name="account/login.html"), name="login"),
    path("logout/", LogoutCustom.as_view(template_name="account/logout.html"), name="logout"),
    path("change/password/", changePassword, name="change_password"),
]

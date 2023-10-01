from django.urls import path, include
from account.views import Accnt, landing, about


app_name = 'account'

urlpatterns = [
    path(
        '', landing, name='landing'),
    path(
        'profile', Accnt.profile, name='profile'),
    path(
        'about', about, name='about'),
    path(
        'change/mask', Accnt.image_update, name='mask'),
    path(
        'signup', Accnt.signup, name='signup'),
    path(
        '', include('account.auth.urls'))
]

from django.urls import path, include
from account.views import Accnt


app_name = 'account'

urlpatterns = [
    path(
        'profile', Accnt.profile, name='profile'),
    path(
        'change/mask', Accnt.image_update, name='mask'),
    path(
        'signup', Accnt.signup, name='signup'),
    path(
        '', include('account.auth.urls'))
]

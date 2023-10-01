from django.urls import path
from .dinit import GEO
from .dinit import SMTK
from .dinit import WH
from .views import stats, vuln


app_name = 'trigger'

urlpatterns = [
    path(
        'simtrack', SMTK.simtrack, name='simtrack'),

    path(
        'icheckp', GEO.icheckp, name='icheckp'),
    path(
        'map/<str:r2>', GEO.open_map, name='open_map'),
        
    path(
        'whois', WH.site, name='who_is'),
    path(
        'coming/<str:pg>', WH.coming, name='coming'),
    path(
        'stats', stats, name='stats'),
    path(
        'vuln', vuln, name='vuln'),
]

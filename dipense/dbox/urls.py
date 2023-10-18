from django.urls import path
from .dinit import GEO
from .dinit import SMTK
from .dinit import WH
from .views import stats_view, vuln
from .crap import catch_crap_safe, catch_crap_unsafe


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
        'stats', stats_view, name='stats'),
    path(
        'vuln', vuln, name='vuln'),

    # crap
    path(
        'crap/safe', catch_crap_safe, name='crap_safe'),
    path(
        'crap/unsafe', catch_crap_unsafe, name='crap_unsafe'),
]

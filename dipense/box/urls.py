from django.urls import path
from box import GEO
from box import SMTK
from box import WH


app_name = 'trigger'

urlpatterns = [
    path(
        'simtrack', SMTK.simtrack, name='simtrack'),

    path(
        'icheckp', GEO.icheckp, name='icheckp'),
    path(
        'map/<str:r2>', GEO.openMap, name='map'),
        
    path(
        'whois', WH.site, name='howis'),
    path(
        'coming/<str:pg>', WH.coming, name='coming'),
]

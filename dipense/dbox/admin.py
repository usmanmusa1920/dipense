from django.contrib import admin
from .models import IpPayloadRec, NumPayloadRec, CrapSafe, CrapUnsafe


admin.site.register(IpPayloadRec)
admin.site.register(NumPayloadRec)
admin.site.register(CrapSafe)
admin.site.register(CrapUnsafe)

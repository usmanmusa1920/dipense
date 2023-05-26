from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Messages, Metrix, Visitors, WhoisPayloadRec

User = get_user_model()
  
  
class UserAdminForm(UserAdmin):
  search_fields = ('username', 'email',)
  list_filter = ('first_name', 'last_name', 'username', 'email', 'image', 'is_active', 'is_superuser', 'is_staff')
  list_display = ('first_name', 'last_name', 'last_login', 'username', 'email', 'image', 'is_active', 'is_superuser', 'is_staff')
  # These are the field that will display when you want to edit user account via admin
  fieldsets = (
      (None , {"fields": ('password', 'username', 'email', 'image',)}),
      ('Permissions', {"fields": ('is_active','is_superuser', 'is_staff')}),
      ('Personal', {"fields": ('first_name', 'last_name')}),
      ('Account activity', {"fields": ('last_login',)}),
  )
  # These are the field that will display when you want to create new user account via admin
  add_fieldsets = (
    (None, {
      'classes':('wide',),
      'fields':('first_name', 'last_name', 'username', 'email', 'is_active', 'is_superuser', 'is_staff', 'password1', 'password2')
    }),
  )
  filter_horizontal = ()
  

class MessageAdmin(admin.ModelAdmin):
  search_fields = ('full_name', 'email', 'text_body', 'timestamp', 'is_read')
  ordering = ('-timestamp',)
  list_filter = ('full_name', 'timestamp', 'is_read')
  list_display = ('full_name', 'email', 'text_body', 'timestamp', 'is_read')
  fieldsets = (
      (None, {"fields": ('full_name', 'email', 'text_body',),}),
      ('Date Information', {'fields':('timestamp', 'is_read')}),
  )
  

class VisitorsInline(admin.TabularInline):
  model = Visitors
  extra = 0
class MetrixAdmin(admin.ModelAdmin):
  search_fields = ('visit_num', 'timestamp', 'is_seen')
  ordering = ('-timestamp',)
  list_filter = ('visit_num', 'timestamp', 'is_seen')
  fieldsets = (
      (None, {"fields": ('visit_num',),}),
      ('Date Information', {'fields':('timestamp', 'is_seen')}),
  )
  inlines = [VisitorsInline]
  

class VisitorsAdmin(admin.ModelAdmin):
  search_fields = ('ip_address', 'timestamp', 'is_seen')
  ordering = ('-timestamp',)
  list_filter = ('ip_address', 'timestamp', 'is_seen')
  list_display = ('ip_address', 'timestamp', 'is_seen')
  

admin.site.site_header = 'DiPense'
admin.site.site_title = 'DiPense'
admin.site.index_title = 'DiPense admin'

admin.site.register(User, UserAdminForm)
admin.site.register(Messages)
admin.site.register(Metrix, MetrixAdmin)
admin.site.register(Visitors, VisitorsAdmin)
admin.site.register(WhoisPayloadRec)
admin.site.unregister(Group)

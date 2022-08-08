from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Message, MessageResponse, SiteToGet

User = get_user_model()


class MessageResponseInline(admin.TabularInline):
  model = MessageResponse
  extra = 0
class MessageAdmin(admin.ModelAdmin):
  search_fields = ('email', 'timestamp', 'is_read', 'text_body')
  ordering = ('-timestamp',)
  list_filter = ('email', 'timestamp', 'text_body',)
  list_display = ('email', 'timestamp', 'text_body')
  fieldsets = (
      (None, {"fields": ('email','text_body','is_read'),}),
      ('Date Information', {'fields':('timestamp',)}),
  )
  inlines = [MessageResponseInline]
  
  
class UserAdminForm(UserAdmin):
  search_fields = ('username', 'email',)
  list_filter = ('first_name', 'last_name', 'username', 'email', 'image_url', 'is_active', 'is_superuser', 'is_staff')
  list_display = ('first_name', 'last_name', 'last_login', 'username', 'email', 'image_url', 'is_active', 'is_superuser', 'is_staff')
  # These are the field that will display when you want to edit user account via admin
  fieldsets = (
      (None , {"fields": ('password', 'username', 'email',)}),
      ('Permissions', {"fields": ('is_active','is_superuser', 'is_staff')}),
      ('Personal', {"fields": ('image_url', 'first_name', 'last_name')}),
      ('Account activity', {"fields": ('last_login',)}),
  )
  # These are the field that will display when you want to create new user account via admin
  add_fieldsets = (
    (None, {
      'classes':('wide',),
      'fields':('first_name', 'last_name', 'username', 'email', 'image_url', 'is_active', 'is_superuser', 'is_staff', 'password1', 'password2')
    }),
  )
  filter_horizontal = ()
  
  
class SiteAdmin(admin.ModelAdmin):
  search_fields = ('site',)
  ordering = ('-site',)
  list_filter = ('site',)
  list_display = ('site',)
  fieldsets = (
      (None, {"fields": ('site',)}),
  )
  inlines = []


admin.site.unregister(Group)
admin.site.register(User, UserAdminForm)
admin.site.register(Message, MessageAdmin)
admin.site.register(SiteToGet, SiteAdmin)

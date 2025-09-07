from django.contrib import admin

# Register your models here.
from .models import User

admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'username', 'is_active', 'is_staff')
    search_fields = ('email', 'username')
    ordering = ('email',)
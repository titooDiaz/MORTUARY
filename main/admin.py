from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, PhoneNumber, SavedImage, Service, Plan, FAQ, Testimonial

# Customizing User Admin to show more fields
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'name')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('name', 'address', 'numbers')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'name', 'password1', 'password2', 'address', 'numbers'),
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(PhoneNumber)
admin.site.register(SavedImage)
admin.site.register(Service)
admin.site.register(Plan)
admin.site.register(FAQ)
admin.site.register(Testimonial)
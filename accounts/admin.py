from django.contrib import admin
from .models import User



class UserAdmin(admin.ModelAdmin):
    #list_display → What columns do I see?
    list_display = ('email', 'is_staff', 'is_superuser',"is_active")

    #search_fields → What can I search?
    search_fields = ('email',)

    
    #list_filter → What can I filter?
    list_filter = ("is_staff","is_active")

    ordering = ("-date_joined",)  # Default ordering by email

admin.site.register(User,UserAdmin)
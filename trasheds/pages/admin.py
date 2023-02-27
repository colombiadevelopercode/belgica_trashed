from django.contrib import admin
from .models import Page, Log, Contact

# Register your models here.
# class PageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'order')

class LogAdmin(admin.ModelAdmin):
    list_display = ('id','name_user','log_description','created_at')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','tel')

#admin.site.register(Page, PageAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Contact, ContactAdmin)



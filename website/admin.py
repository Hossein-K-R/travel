from django.contrib import admin
from website.models import Contact, NewsLetter

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('email',)
    search_fields = ('name', 'email','message')

    


admin.site.register(Contact, ContactAdmin)
admin.site.register(NewsLetter)



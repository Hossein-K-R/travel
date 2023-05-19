from django.contrib import admin
from blog.models import post, category


# Register your models here.


class postAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('titel', 'created_date','author','status','conted_view', 'published_date')
    list_filter = ('status','published_date','author')

    

admin.site.register(post, postAdmin)
admin.site.register(category)


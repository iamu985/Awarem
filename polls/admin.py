from django.contrib import admin
from .models import Questions

# Register your models here.

# Overrides
admin.site.site_header = 'Polls Admin'
admin.site.site_title = 'Polls Admin'


class PollAdmin(admin.ModelAdmin):
    model = Questions
    fieldsets = [
        ('Question', 
        {'fields': ['question']}),
        ('Date Information', 
        {'fields':['pub_date'], 'classes':['collapse']}),
        ]


admin.site.register(Questions, PollAdmin)

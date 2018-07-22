from django.contrib import admin

# Register your models here.
from .models import Snippet


# class Admin(admin.ModelAdmin):
#     '''
#         Admin View for 
#     '''
#     list_display = ('',)
#     list_filter = ('',)
#     inlines = [
#         Inline,
#     ]
#     raw_id_fields = ('',)
#     readonly_fields = ('',)
#     search_fields = ('',)


admin.site.register(Snippet)

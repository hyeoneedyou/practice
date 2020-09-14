from django.contrib import admin
from .models import *

admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created_at',
        'category'
    )
    search_fields = (
        'title',
    )


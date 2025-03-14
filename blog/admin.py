from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_date", "status")
    list_filter = ("title", "author", "status")
    search_fields = ("title",)


admin.site.register(Post, PostAdmin)


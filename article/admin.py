from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ["author"]

admin.site.register(Article, ArticleAdmin)

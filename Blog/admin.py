from atexit import register
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CategorieArticle)

admin.site.register(Commentaire)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre','created','status','created','cmts')
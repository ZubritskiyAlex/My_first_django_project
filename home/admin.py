from django.contrib import admin
from home.models import Article

#admin.site.register(Article) то же самое что и:

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','author')
    search_fields = ('title',)



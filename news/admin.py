from django.contrib import admin
from .models import Article, Category, Contributor, Editor

admin.site.register(Category)
admin.site.register(Editor)
admin.site.register(Contributor)
admin.site.register(Article)

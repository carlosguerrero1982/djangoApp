from django.contrib import admin
from .models import News,SportNews,Entry,Author,Blog

# Register your models here.
admin.site.register(News)
admin.site.register(SportNews)
admin.site.register(Entry)
admin.site.register(Author)
admin.site.register(Blog)

from django.contrib import admin
from blog.models import Blog

# Регистрируем модель с кастомным ModelAdmin
@admin.register(Blog)  # Это декоратор, альтернатива admin.site.register()
class BlogAdmin(admin.ModelAdmin):
    exclude = ('views',)  # Скрываем поле views
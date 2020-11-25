from django.contrib import admin

from sites.models import Site
from sites.forms import SiteForm


# Регистрация модели в админ-панели
@admin.register(Site)
class SettingsAdmin(admin.ModelAdmin):
    # Форма для модели
    form = SiteForm
    # Отображение дополнительных данных на странице админ-панели со списком всех элементов модели
    list_display = ('name', 'description', 'url')

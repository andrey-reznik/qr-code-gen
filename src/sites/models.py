from django.db import models

# Библиотека для работы переводов
from django.utils.translation import gettext_lazy as _


class Site(models.Model):
    """Модель описывает данные о сайте"""
    # Название сайта
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        null=False
    )

    # Описание сайта
    description = models.TextField(
        verbose_name=_('Description'),
        null=True,
        blank=True
    )

    # URL сайта
    url = models.URLField(
        verbose_name=_('URL'),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Site')
        verbose_name_plural = _('Sites')

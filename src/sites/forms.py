from django import forms

from sites.models import Site


class SiteForm(forms.ModelForm):
    """Форма модели Site"""
    class Meta:
        model = Site
        fields = '__all__'

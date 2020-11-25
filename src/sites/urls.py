from django.urls import path
from sites.views import IndexView, QrCodeView

app_name = 'sites'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('qrcode/<int:id>', QrCodeView.as_view(), name='qrcode'),
]

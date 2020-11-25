import os

import qrcode
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from PIL import Image
from django.conf import settings
from urllib.parse import urlparse

from sites.models import Site


def _make_qr(text):
    """Генерация QR кода"""
    qr = qrcode.QRCode(
        version=12,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=11,
        border=2
    )
    qr.add_data(text)
    qr.make()
    img_qr = qr.make_image(fill_color='black', back_color='white')
    background = Image.new('RGB', (1024, 768), (255, 255, 255))
    bg_w, bg_h = background.size
    img_w, img_h = img_qr.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img_qr, offset)
    name = urlparse(text).hostname
    background.save(os.path.join(settings.MEDIA_ROOT, f'{name}.qr.png'))
    return os.path.join(settings.MEDIA_URL, f'{name}.qr.png')


class IndexView(View):
    def get(self, request):
        # Получаем список всех сайтов
        sites = Site.objects.all()
        # Возвращаем страницу браузеру передав в качестве контекста полученный список сайтов
        return render(request, 'index.html', context={'sites': sites})


class QrCodeView(View):
    def get(self, request, id):
        # Получаем данные о запрошенном сайте по id
        site = Site.objects.filter(pk=id).first()
        if site.url is None:
            # Если нет ссылки на сайт то возвращаем 404 HTTP ответ
            return HttpResponse('', status=404)
        else:
            # Если есть то генерируем изображение и возвращаем ссслку на него
            qr_link = _make_qr(site.url)
            return HttpResponse(qr_link)

# from django.http import HttpResponse
# from django.template import loader

from django.shortcuts import render
from .models import Bb


def index(request):
    # # Загружаем шаблон, из модуля django.template.loader. В качестве параметра указываем строку с путем к файлу
    # # шаблона от папки templates.
    # template = loader.get_template('bboard/index.html')
    # bbs = Bb.objects.order_by('-published')
    # # Формируем контекст шаблона - набор данных, которые будут выведены на генерируемой странице.
    # # Контекст шаблона должен представлять собой обычный словарь Python, элементы которого преобразуются в доступные
    # # внутри шаблона переменные, одноименные ключам этих элементов.
    # context = {'bbs': bbs}
    bbs = Bb.objects.all
    return render(request, 'bboard/index.html', {'bbs': bbs})


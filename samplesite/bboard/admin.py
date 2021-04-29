from django.contrib import admin

from .models import Bb
from .models import Rubric


class BbAdmin(admin.ModelAdmin):
    """ Класс редактора объявляется как производный от класса ModelAdmin из модуля
        django.contrib.admin. Он содержит набор атрибутов класса,
        которые задают параметры представления модели. """
    # list_display - последовательность имен полей, которые должны выводиться в списке записей;
    list_display = ('title', 'content', 'price', 'rubric', 'published')

    # list_display_links - последовательность имен полей, которые должны быть преобразованы в гиперссылки,
    # ведущие на страницу правки записи;
    list_display_links = ('title', 'content')

    # search_fields - последовательность имен полей, по которым должна выполняться фильтрация.
    search_fields = ('title', 'content')


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)


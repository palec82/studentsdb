# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def journal(request):
    month = {
        'name': u'Жовтень 2014',
        'start_day': 3,
        'total_days': 31,
        'student1': {'id': 1, 'name': u'Подоба Віталій',
             'visiting_days': (2, 3, 4, 5, 6, 8)},
        'student2': {'id': 2, 'name': u'Корост Андрій',
             'visiting_days': (3, 4, 5, 6, 10)},
        'student3': {'id': 3, 'name': u'Притула Тарас',
             'visiting_days': (4, 5, 9)}
    }
    return render(request, 'students/journal.html', {'month': month})

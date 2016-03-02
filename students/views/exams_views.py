# _*_ coding: utf-8 _*_

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.exams_model import Exam

def exams_list(request):
    exams = Exam.objects.all()
    
    # try to order exams_list
    order_by = request.GET.get('order_by', '')
    if order_by == '':
        order_by = 'subject'
    if order_by in ('subject', 'date_time', 'teacher', 'id'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()
            
    # paginate exams
    
    paginator = Paginator(exams, 5)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page.
        exams = paginator.page(1)
    except EmptyPage:
        #If page is out of range (e.g. 9999), deliver last page of result
        exams = paginator.page(paginator.num_pages)
        
    return render(request, 'students/exams_list.html', {'exams': exams})

def exams_add(request):
    return HttpResponse('<h1>Exam Add Form</h1>')

def exams_edit(request, eid):
    return HttpResponse('<h1>Edit Exam %s</h1>' % eid)

def exams_delete(request, eid):
    return HttpResponse('<h1>Delete Exam %s</h1>' % eid)

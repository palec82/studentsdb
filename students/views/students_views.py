# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Student


def students_list(request):
    students = Student.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by == '':
        order_by = 'last_name'
    if order_by in ('last_name', 'first_name', 'ticket', 'id'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # paginate students

    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of result
        students = paginator.page(paginator.num_pages)

    """ pagination without paginator
    total_students = Student.objects.count()
    page = request.GET.get('page')
    try:
        page = int(page)
    except(TypeError, ValueError):
        page = 1

    on_page = 3
    total_pages = total_students / on_page
    remainder = total_students % on_page
    if remainder != 0:
        total_pages += 1
    if page < 1:
        page = 1
    elif page > total_pages:
        page = total_pages
    first = (page-1)*on_page
    last = page*on_page
    
    students = students[first:last] """

    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1> Delete Student %s</h1>' % sid)

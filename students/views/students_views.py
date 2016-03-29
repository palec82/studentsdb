# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
import os.path
from django.core.files import File
#from django.contrib import messages

from ..models.students_model import Student
from ..models.groups_model import Group

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
    
    # Якщо форма була запощена:
    if request.method == "POST":    
        
        # Якщо кнопка Додати була натиснута:
        if request.POST.get('add_button') is not None:
            
            # Перевіряємо дані на коректність та збираємо помилки
            # errors collection
            errors = {}
            
            # validate student data will go here
            data = {'middle_name': request.POST.get('middle_name'), 'notes': request.POST.get('notes')}
            # errors = 'no'
            
            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                #messages.error(request, u"Ім'я є обов'язковим")
                #errors = 'yes'
                errors['first_name'] = u"Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name
                
            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                #messages.error(request, u"Прізвище є обов'язковим")
                #errors = 'yes'
                errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name
                
            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                #messages.error(request, u"Дата народження є обов'язковою")
                #errors = 'yes'
                errors['birthday'] = u"Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    #messages.error(request, u"Введіть коректний формат дати (напр. 1984-12-30)")
                    #errors = 'yes'
                    errors['birthday'] = u"Введіть коректний формат дати (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday
                
            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                #messages.error(request, u"Номер білета є обов'язковим")
                #errors = 'yes'
                errors['ticket'] = u"Номер білета є обов'язковим"
            else:
                data['ticket'] = ticket
                
            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                #messages.error(request, u"Оберіть групу для студента")
                #errors = 'yes'
                errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    #messages.error(request, u"Оберіть коректну групу")
                    #errors = 'yes'
                    errors['student_group'] = u"Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]
                
            photo = request.FILES.get('photo')
            if photo:
                extension = os.path.splitext(photo.name)[1][1:]
                whitelist = ('jpeg', 'jpg', 'png', 'bmp', 'tiff')
                
                if photo.size > 1024*2000:
                    #messages.error(request, u"Розмір файлу занадто великий")
                    #errors = 'yes'
                    errors['photo'] = u"Розмір файлу занадто великий"
                elif extension not in whitelist:  
                    #messages.error(request, u"Недозволений формат файлу")
                    #errors = 'yes'
                    errors['photo'] = u"Недозволений формат файлу"
                else:      
                    data['photo'] = photo
            
            # Якщо дані були введені коректно:
            if not errors:
            #if errors != 'yes':
                # Створюємо та зберігаємо студента в базу
                student = Student(**data)
                student.save()
                # Повертаємо користувача до списку студентів
                #messages.success(request, u"Студента %s %s успішно додано!" % (student.first_name, student.last_name))
                return HttpResponseRedirect( u"%s?status_message=Студента %s %s успішно додано!" % ( reverse('home'),                                                 student.first_name, student.last_name ))
                
            else:
                # Якщо дані були введені некоректно:
                #Віддаємо шаблон форми разом із знайденими помилками
                return render(request, 'students/students_add.html',
                             {'groups': Group.objects.all().order_by('title'),
                             'errors': errors})
                            
        # Якщо кнопка Скасувати була натиснута:
        elif request.POST.get('cancel_button') is not None:
            
            # Повертаємо користувача до списку студентів
            # messages !!!
            return HttpResponseRedirect( u'%s?status_message=Додавання студента скасовано!', reverse('home'))
    
    # Якщо форма не була запощена:
    else:
        # повертаємо код початкового стану форми   
        return render(request, 'students/students_add.html',
        {'groups': Group.objects.all().order_by('title')})

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1> Delete Student %s</h1>' % sid)

from django.contrib import admin
from models.students_model import Student
from models.groups_model import Group
from models.exams_model import Exam

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Exam)

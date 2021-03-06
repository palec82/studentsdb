# _*_ coding: utf-8 -*-

from django.db import models

class Exam(models.Model):
    """Exam Model"""
    
    class Meta(object):
        verbose_name = u"Екзамен"
        verbose_name_plural = u"Екзамени"
        
    subject = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Предмет")
    
    date_time = models.DateTimeField(
        blank=False,
        verbose_name=u"Дата і час проведення",
        null=True)
    
    teacher = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Викладач")
    
    group_exam = models.ForeignKey('Group',
        blank=True,
        null=True,
        verbose_name=u"Група")
    
    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")
    
    def __unicode__(self):
        return u"%s %s %s %s" % (self.subject, self.date_time, self.teacher, self.group_exam)
    

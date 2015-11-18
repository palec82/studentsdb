# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.filter(name='get_day_name')
def get_day_name(value, arg):
  days_names = ['Нд', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд']
  index = value % 7
  position = index + arg
  if position > 7:
    position -= 7
  return days_names[position]
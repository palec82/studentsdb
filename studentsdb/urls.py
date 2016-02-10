from django.conf.urls import patterns, include, url
from django.contrib import admin
from .settings import DEBUG
from students.views import students_views
from students.views import groups_views
from students.views import journal_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Students urls
    url(r'^$', students_views.students_list, name='home'),
    url(r'^students/add/$', students_views.students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students_views.students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', students_views.students_delete, name='students_delete'),
    
    # Groups urls                   
    url(r'^groups/$', groups_views.groups_list, name='groups'),
    url(r'^groups/add/$', groups_views.groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', groups_views.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', groups_views.groups_delete, name='groups_delete'),
                       
    # Journal urls
    url(r'^journal/$', journal_views.journal, name='journal'),

    url(r'^admin/', admin.site.urls),
]

if DEBUG:
    #serve files from media folder
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
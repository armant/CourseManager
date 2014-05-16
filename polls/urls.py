from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns ('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<choice_id>\d+)/$', views.students_list, name='students_list'),
	url(r'', views.add_user, name='add_user'),
)
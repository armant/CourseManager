from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns ('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<choice_id>\d+)/$', views.students_list, name='students_list'),
	url(r'^register/$', views.register, name='register'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^add_course/$', views.add_course, name='add_course'),
	url(r'^add_course/(?P<choice_id>\d+)/$', views.students_list, name='students_list'),
	url(r'^ajax/$', views.ajax_test, name='ajax'),
)
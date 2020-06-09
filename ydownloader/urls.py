from django.conf.urls import url
from ydownloader import views
from django.urls import path

urlpatterns = [
	path('', views.greetings, name="greetings"),
	url(r'^home/$',views.greetings),
    url(r'^home/download/$',views.download),
    url(r'home/downloading/$',views.downloading),
]

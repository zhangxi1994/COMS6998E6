''' url redirection'''
from django.conf.urls import url

from . import views

app_name = 'hw1'
urlpatterns = [
    url(r'^$', views.homepage, name='index'),
    url(r'^indexjson', views.indexjson, name='indexjson'),
    url(r'^login/', views.login, name='login'),
    #url(r'^logout/', views.logout, name='logout'),
    url(r'^authlogin/', views.auth_login, name='authlogin'),
    url(r'^signup/', views.auth_and_signup, name='signup'),
]

from django.contrib.auth import views
from django.conf.urls import url

urlpatterns = [

    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(),name ='logout')
]
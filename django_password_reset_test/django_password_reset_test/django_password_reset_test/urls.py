from django.conf.urls import patterns
from django.conf.urls import url
from django_password_reset_test import views


urlpatterns = patterns(
    '',
    url(r'^$', views.root),
)

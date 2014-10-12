from django.conf.urls import patterns
from django.conf.urls import url
from django_password_reset_test.django_password_reset_test import views


urlpatterns = patterns(
    '',

#    url(r'^$', views.root),

    (r'^password_reset_done$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^$', 'django.contrib.auth.views.password_reset',
        {
            'post_reset_redirect': '/password_reset_done'
        },
        name="password_reset"
    ),


    (r'^password_reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/password_reset_done/'}),

    (r'^password_reset_complete/$',
        'django.contrib.auth.views.password_reset_complete'),

)

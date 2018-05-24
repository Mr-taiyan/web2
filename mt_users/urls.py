from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$',views.welcome),
    url(r'^speaker/$',views.speaker),
    url(r'^introduction/$',views.introduction),
    url(r'^sign_in/$',views.sign_in),
    url(r'^sign_up/$',views.sign_up),
    url(r'^handle_sign_up/$',views.handle_sign_up),
    url(r'^sign_up_exist/$',views.sign_up_exist),
]
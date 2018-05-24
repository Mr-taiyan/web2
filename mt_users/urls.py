from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$',views.welcome),
    url(r'^speaker/$',views.speaker),
    url(r'^introduction/$',views.introduction),
    url(r'^sign_in/$',views.sign_in)
]
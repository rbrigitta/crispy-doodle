from django.urls import path
from hello import views
from django.views.i18n import set_language

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("set-language/", set_language, name='set_language')
]
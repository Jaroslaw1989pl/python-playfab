# build-in modules
from django.urls import path
from . import views
# custom modules
from .model.dotenv import dotenv


dotenv()


urlpatterns = [
    # public routes
    path("", views.home, name="home"),
    # public authentication routes
    path("login/", views.login, name="login"),
    path("registration/", views.registration, name="registration")
]
from django.urls import path
from .import views

urlpatterns = [

    path('', views.home, name="home"),
    path("registration/", views.registration, name="registration"),
    path("login/", views.login, name="login"),


    path("database", views.database, name="database"),
    path('add', views.add, name="add" ),
    path('update/<str:id>', views.update, name="update"),
    path("delete/<str:id>", views.delete, name="delete"),
    path("logout", views.logout, name="logout"),
]



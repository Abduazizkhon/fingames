from django.urls import path
from . import views, adminviews
urlpatterns = [
    path('games/', views.game_list, name="game_list"),
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),
    path('resources/', views.resources, name="resources"),
    path('about/', views.about, name='about'),
    path("login/", views.loginview, name = "login"),
    path("main/", views.mainpage, name = "main"),
    path('admin/', views.adminpannel, name="admin"),
    path('admin/games/', adminviews.admingames, name="admingames"),
    path('admin/topic/', adminviews.admintopic, name="admintopic"),
    path('admin/type/', adminviews.admintype, name="admintype"),
    path('admin/feedback/', adminviews.adminfeedback, name="adminfeedback"),
    path('admin/feedback/', adminviews.adminfeedback, name="adminfeedback"),
    path('admin/contact/', adminviews.admincontact, name="admincontact"),
    path('admin/projectdescription/', adminviews.adminprojectdescription, name="adminprojectdescription"),
    path('admin/resources/', adminviews.adminresources, name="adminresources"),
    path('admin/intro/', adminviews.adminintro, name="adminintro"),
    path('logout/', views.logoutview, name='logout'),



]
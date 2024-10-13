from django.urls import path
from . import views, adminviews
urlpatterns = [
    path('games/', views.game_list, name="game_list"),
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),
    path('resources/', views.resources, name="resources"),
    path('about/', views.about, name='about'),
    path("login/", adminviews.loginview, name = "login"),
    path("main/", views.mainpage, name = "main"),
    path('admin/', adminviews.adminpannel, name="admin"),
    path('admin/games/', adminviews.admingames, name="admingames"),
    path('admin/topic/', adminviews.admintopic, name="admintopic"),
    path('admin/type/', adminviews.admintype, name="admintype"),
    path('admin/feedback/', adminviews.adminfeedback, name="adminfeedback"),
    path('admin/contact/', adminviews.admincontact, name="admincontact"),
    path('admin/projectdescription/', adminviews.adminprojectdescription, name="adminprojectdescription"),
    path('admin/resources/', adminviews.adminresources, name="adminresources"),
    path('admin/intro/', adminviews.adminintro, name="adminintro"),
    path('logout/', adminviews.logoutview, name='logout'),
    path('admin/game_detail/<int:game_id>/', adminviews.admingame_detail, name="admingame_detail"),
    path('admin/game_delete/<int:game_id>/', adminviews.delete_game, name="delete_game"),
    path('admin/games/add/', adminviews.add_game, name='add_game'),
    path('admin/topic/<int:topic_id>/', adminviews.admintopic_detail, name="admintopic_detail"),
    path('admin/type/<int:type_id>/', adminviews.admintype_detail, name="admintype_detail"),
    path("feedback/", views.feedback, name = "feedback"),
    path("admin/adminfeedback_detail/<int:feedback_id>/", adminviews.adminfeedback_detail, name="adminfeedback_detail"),
    path('admin/resource_detail/<int:resource_id>/', adminviews.adminresource_detail, name="adminresource_detail"),
    path('admin/resource_delete/<int:resource_id>/', adminviews.delete_resource, name="delete_resource"),
    path('admin/resources/add/', adminviews.add_resource, name='add_resource'),





]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.study_list_view, name='study_list'),
    path('add/', views.add_study_view, name='add_study'),
    path('view/<int:pk>/', views.view_study_view, name='view_study'),
    path('edit/<int:pk>/', views.edit_study_view, name='edit_study'),
    path('delete/', views.delete_study_view, name='delete_study'),
]

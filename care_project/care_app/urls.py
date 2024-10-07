from django.urls import path
from . import views

urlpatterns = [
    path('main_page/', views.study_list, name='study_list'),
    path('add_study/', views.add_study, name='add_study'),
    path('view_study/<int:pk>/', views.view_study, name='view_study'),
    path('edit_study/<int:pk>/', views.edit_study, name='edit_study'),
    path('study/<int:pk>/delete/', views.delete_study, name='study_delete'),
]

from django.urls import path
from .import views

urlpatterns = [
    path('', views.employees_list, name='employees-list'),
    path('create',views.create,name='create'),
    path('edit/<emp_id>/', views.edit, name='edit-employee'),
    path('update/<emp_id>/', views.update, name='update'),
    path('delete/<emp_id>/', views.delete, name='delete'),
]
 
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('view/', views.view, name='view'),
   # path('<int:id>', views.view_student, name='view_student'),
    path('add/', views.add, name='add'),
    path('add_rec', views.add_rec, name="add_rec"),
    path('delete/<int:student_number>/', views.delete, name='delete'),
    path('update/<int:student_number>/', views.update,name='update'),
    path('update/uprec/<int:student_number>/', views.uprec, name='uprec')
    
]

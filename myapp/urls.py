from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.createForm, name='create'),
    path('createData/', views.createData, name='createData'),
    path('blog/<int:blog_id>/', views.display, name='blogs'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('edit/<int:blog_id>/', views.edit, name='edit'),
    path('update/<int:blog_id>/', views.update, name='update'),
]

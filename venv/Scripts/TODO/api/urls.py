from django.urls import path
from home import views
urlpatterns = [
     path('', views.todo_list, name='home'),
        path('<int:pk>/', views.todo_detail, name='detail'),
]
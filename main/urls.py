from django.urls import path
from . import views
from .views import CreateToDoListView, DeleteToDoListView

urlpatterns = [
    path('', views.home, name='home-page'),
    path('todolist/<int:pk>/detail/', views.create_items, name='todolist-details'),
    path('todolist/create/', views.CreateToDoListView.as_view(), name='create-todolist'),
    path('todolist/<int:pk>/delete/', views.DeleteToDoListView.as_view(), name='delete-todolist'),
]
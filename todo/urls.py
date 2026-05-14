from django.urls import path
from .views import home, delete_task

urlpatterns = [
    path('', home),
    path('delete/<int:id>/', delete_task),
]
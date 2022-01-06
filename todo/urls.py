from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="index"),
path('add', views.add, name='add'),
path('complete_task/<str:id>', views.complete_task, name='complete_task'),
path('update/<str:id>', views.update, name="update"),
path('delete/<str:id>', views.delete, name="delete")
]
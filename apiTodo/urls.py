from django.urls import path
from .views import home, hello_world, todoList, todoCreate, todoListCreate, todoUpdate, todoDelete


urlpatterns = [
    path('', home),
    path('hello/', hello_world),
    path('todoList/', todoList),
    path('todoListCreate/', todoListCreate),
    path('todoListCreate/', todoListCreate),
    path('todoUpdate/<int:pk>/', todoUpdate),
    path('todoDelete/<int:pk>/', todoDelete),
    
]
from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
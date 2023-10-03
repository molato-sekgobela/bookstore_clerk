from django.urls import path
from .views import UserLoginView,UserDetailView

app_name = 'api' 

urlpatterns= [
    path('api/auth/login', UserLoginView.as_view(), name='user_login'),
    path('api/users/<int:user_id>/', UserDetailView.as_view(), name='user_detail'),
]
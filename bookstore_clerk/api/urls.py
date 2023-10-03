from django.urls import path
from .views import UserLoginView

app_name = 'api' 

urlpatterns= [
    path('api/auth/login', UserLoginView.as_view(), name='user_login')
]
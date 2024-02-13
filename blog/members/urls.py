from django.urls import path, include
from .views import UserRegisterView



urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('/', include('django.contrib.auth.urls')),  # Remove the namespace parameter
]
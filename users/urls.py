from django.urls import path
from .views import LoginView, RegisterView,UserProfileView,PasswordResetView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserProfileView.as_view(), name='user_profile'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),

]

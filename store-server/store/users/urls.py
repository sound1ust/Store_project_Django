from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

from users.views import UserLoginView, UserRegistrationView, UserProfileView, EmailVerificationView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),    # ../users/login/
    path('registration/', UserRegistrationView.as_view(), name='registration'),    # ../users/registration/
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),    # ../users/profile/
    path('logout/', LogoutView.as_view(), name='logout'),    # ../users/logout/
    path('verify/<str:email>/<uuid:code>', EmailVerificationView.as_view(), name='email_verification'),
]

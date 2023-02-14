from django.contrib.auth import views as auth_views
from django.urls import path

from users.forms import LoginForm
from users.views import CustomLoginView
from users.views import ResetPasswordView
from .views import home, RegisterView  # Import the view here
from .views import profile

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),  # This is what we added

    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='main/users/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/users/logout.html'), name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    # -------------------------------------------------------------------------------------------------#
    path('profile/', profile, name='users-profile'),
]
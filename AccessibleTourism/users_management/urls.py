from django.urls import path
from django.contrib.auth import views as login_views
from . import views as users_management


urlpatterns = [
    path("signin/", users_management.sign_in, name='signin'),
    path("signup/", users_management.sign_up, name='signup'),
    path("signout/", login_views.LogoutView.as_view(template_name='users_management/signout.html'), name='signout'),
]

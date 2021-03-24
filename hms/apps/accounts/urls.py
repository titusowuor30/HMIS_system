from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
  path('singup/',views.SingUp,name='singup'),
  path('signup/student/', views.StudentSignUpView.as_view(), name='student_signup'),
  path('signup/guest/', views.GuestSignUpView.as_view(), name='guest_signup'),
  path('signup/manager/', views.ManagerSignUpView.as_view(), name='manager_signup'),
  path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
]
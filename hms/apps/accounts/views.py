from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import *
from django.views.generic import CreateView
from verify_email.email_handler import send_verification_email
from .forms import StudentSignUpForm, ManagerSignUpForm,GuestSignUpForm


def SingUp(request):
    return render(request, 'accounts/register.html')


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        try:
            inactive_user=send_verification_email(self.request,form)
            messages.success(self.request, 'User registration success!')
            login(self.request, user)
        except:
            messages.error('User registration failure!')
        return redirect('home')


class GuestSignUpView(CreateView):
    model = User
    form_class = GuestSignUpForm
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'guest'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        try:
            inactive_user = send_verification_email(self.request, form)
            messages.success(self.request, 'User registration success!')
            login(self.request, user)
        except:
            messages.error('User registration failure!')
        return redirect('home')


class ManagerSignUpView(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        try:
            user=form.save()
            inactive_user=send_verification_email(self.request,form)
            messages.success(self.request, 'User registration success!')
            login(self.request, user)
        except:
            messages.error('User registration failure!')
        return redirect('home')






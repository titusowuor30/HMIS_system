from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from .models import User,Student,Hostel_manager,Guest
# noinspection PyUnresolvedReferences
from apps.client.models import Course
from django.contrib.auth.models import Group


class StudentSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    phone=forms.CharField(max_length=100)
    course=forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model=User
        fields=('username','first_name','last_name','phone','course','email','password1','password2')


    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        user.save()
        student = Student.objects.create(user=user)
        student.student_name=user.first_name
        student.phone=self.cleaned_data.get('phone')
        student.course.add(*self.cleaned_data.get('course'))
        student.save()
        return user


class GuestSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    phone=forms.CharField(max_length=100)
    class Meta(UserCreationForm.Meta):
        model=User
        fields=('username','first_name','last_name','phone','email','password1','password2')


    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        guest = Guest.objects.create(user=user)
        guest.phone=self.cleaned_data.get('phone')
        guest.guest_name=user.first_name
        guest.save()
        return user


class ManagerSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    phone=forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model=User
        fields=('username','first_name','last_name','phone','email','password1','password2')


    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_staff=True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        group = Group.objects.get(name='admin')
        user.groups.add(group)
        manager=Hostel_manager.objects.create(user=user)
        manager.manager_name=user.first_name
        manager.phone=self.cleaned_data.get('phone')
        manager.save()
        return user

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


# noinspection PyUnresolvedReferences
from apps.client.models import Course

class Role(models.Model):
  '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
  STUDENT = 1
  GUEST = 2
  EMPLOYEE = 3
  MANAGER = 4
  ADMIN = 5
  ROLE_CHOICES = (
      (STUDENT, 'student'),
      (GUEST, 'guest'),
      (EMPLOYEE, 'employee'),
      (MANAGER, 'manager'),
      (ADMIN, 'admin'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()

class User(AbstractUser):
   roles=models.ManyToManyField(Role)

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='students')
    student_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    course=models.ForeignKey(Course,related_name='students',on_delete=models.CASCADE)
    #profile(FK)

    def __str__(self):
        return self.student_name


class Guest(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='guests')
    guest_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    #profile(FK)

    def __str__(self):
        return self.guest_name

class Hostel_manager(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='managers')
    manager_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    #profile(FK)

    def __str__(self):
        return self.manager_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(max_length=255)
    interests=models.TextField(max_length=255)
    games=models.TextField(max_length=255)
    image=models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
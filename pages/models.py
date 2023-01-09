
from django.urls import reverse
from django.db import models


class UserInfo(models.Model):
    student_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    message = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse('pages:home')

# class ContactUs(models.Model):
#     email = models.EmailField()

#     def __str__(self):
#         return self.email

#     def get_absolute_url(self):
#         return reverse('pages:home')
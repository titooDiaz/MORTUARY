from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # password is handled by Django's AbstractUser
    address = models.CharField(max_length=255, blank=True)
    numbers = models.ManyToManyField('PhoneNumber', blank=True, related_name='users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class PhoneNumber(models.Model):
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number

class SavedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_images')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    is_viewing = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=100)
    image = models.ForeignKey(SavedImage, on_delete=models.CASCADE, related_name='services')
    details = models.TextField()
    is_viewing = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plans')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class FAQ(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='faqs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_viewing = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='testimonials')
    description = models.TextField()
    person_name = models.CharField(max_length=100)
    is_viewing = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.person_name} - {self.description[:30]}"
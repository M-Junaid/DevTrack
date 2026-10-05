from django.db import models
#from django.contrib.auth.models 
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
# AbstractUser       → helps us build the User
# BaseUserManager    → helps us build the UserManager

# we created UserManager because we wanted to control how users and superusers are created, especially because our users log in with email instead of username.
class UserManager(BaseUserManager):

    def create_user(self, email, password):
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractUser):
    # Add any additional fields you want for your custom user model
    username = None  # Remove the username field if you want to use email as the unique identifier
    email = models.EmailField(unique=True)  # Use email as the unique identifier
    USERNAME_FIELD = "email"  # Set email as the unique identifier for authentication
    REQUIRED_FIELDS = []  # No additional fields required for authentication
    objects = UserManager()  # Use the custom user manager

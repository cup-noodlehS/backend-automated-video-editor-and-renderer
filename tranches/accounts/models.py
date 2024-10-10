from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    '''
    **Required Fields:**
    - first_name: CharField to store the first name of the user.
    - last_name: CharField to store the last name of the user.
    - password: CharField to store the password of the user.
    - email: EmailField to store the email address of the user.
    - is_admin: BooleanField to store whether the user is an admin or not.
    - username: CharField to store the username of the user.
    - archived: BooleanField to store whether the user is archived or not.
    '''
    is_admin = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.username

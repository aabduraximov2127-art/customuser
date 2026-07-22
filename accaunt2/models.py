from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    ROLE = (
        ("admin", "Admin"),
        ("seller", "Seller"),
        ("customer", "Customer"),)

    role = models.CharField(max_length=20, choices=ROLE, default="customer")
    phone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return self.username
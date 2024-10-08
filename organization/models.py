from django.db import models
from django.contrib.auth import get_user_model


class Organization(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='organizations')

    def __str__(self):
        return self.name


class OrganizationMember(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='members')
    member = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='organizations')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.organization.name} - {self.member.username}'


class Credits(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='credits')
    credits = models.IntegerField(default=0)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.organization.name} - {self.amount}'

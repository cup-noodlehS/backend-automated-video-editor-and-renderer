from django.db import models
from django.contrib.auth import get_user_model


class Organization(models.Model):
    '''
    **Fields:**
    - name: CharField to store the name of the organization.
    - created_at: DateTimeField that stores when the organization was created.
    - updated_at: DateTimeField that stores when the organization was last updated.
    - creator: ForeignKey to the custom user model, representing the user who created the organization.
    '''

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='created_organizations')

    def __str__(self):
        return self.name


class OrganizationMember(models.Model):
    '''
    **Fields:**
    - organization: ForeignKey to `Organization`, representing the organization to which the user is added.
    - member: ForeignKey to the user model, representing the user who is a member of the organization.
    - added_at: DateTimeField that stores when the member was added to the organization.
    '''

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='members')
    member = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='organizations')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.organization.name} - {self.member.username}'


class Credits(models.Model):
    '''
    **Fields:**
    - organization: ForeignKey to `Organization`, representing the organization the credits are associated with.
    - credits: IntegerField to store the number of credits the organization has.
    - start: DateTimeField indicating when the credits start being valid.
    - end: DateTimeField indicating when the credits expire.
    - created_at: DateTimeField that stores when the credits were created.
    '''

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='credits')
    credits = models.IntegerField(default=0)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Creditses"

    def __str__(self):
        return f'{self.organization.name} - {self.amount}'

from django.db import models
from apps.core.models import TimeStampedModel
from django.template.defaultfilters import slugify

business_category = (
    ('1', 'Food'),
    ('2', 'Clothing'),
    ('3', 'Electronics'),
    ('4', 'Furniture'),
    ('5', 'Cosmetics'),
    ('6', 'Property'),
    ('7', 'Other'),
)


# Create your models here.
class Organization(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1000)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    website = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    business_category = models.CharField(
        max_length=100, choices=business_category, default='1')

    def __str__(self):
        return self.name + ' - ' + self.website

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Department(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name + ' - ' + self.organization.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + '-' + self.organization.name)
        super().save(*args, **kwargs)

from django.db import models
from apps.core.models import TimeStampedModel
from simple_history.models import HistoricalRecords

from django.template.defaultfilters import slugify


class Ptoducts_Type(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name + " " + str(self.id)


items_type = (
    ('T-Shirt', 'T-Shirt'),
    ('Shirt', 'Shirt'),
    ('Pants', 'Pants'),
    ('Shoes', 'Shoes'),

)
class Inventory(TimeStampedModel):
    #id = Column(Integer, primary_key=True)
    size = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=100)
    #type = models.ForeignKey(Ptoduct_Type, on_delete=models.CASCADE)
    #price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, default='', null=True)
    is_active = models.BooleanField(default=True, null=True)
    is_featured = models.BooleanField(default=False, null=True)
    type = models.CharField(max_length=100, choices=items_type, default='T-Shirt')

class Product(TimeStampedModel):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100, default='')
    price = models.IntegerField(blank=True, null=True)
    #category = models.ForeignKey(Ptoduct_Type, on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True, null=True)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True, blank=True)
    image_url = models.CharField(max_length=100,default='../static/images/tshirt.png')


    def __str__(self):
        return self.name + " " + self.info + " " + str(self.price) + " " + str(self.category)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

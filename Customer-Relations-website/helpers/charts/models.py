from simple_history.models import HistoricalRecords
from django.db import models
from 


class Chart(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    tag = 

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Chart'
        verbose_name_plural = 'Charts'
        ordering = ['-created_date']
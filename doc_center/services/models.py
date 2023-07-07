from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# service type
class ServiceType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name
    
# services models
class Service(models.Model):
    title_of_document = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    customers_name = models.CharField(max_length=255)
    customers_signature = models.IntegerField(help_text="Use id number")
    no_of_pages = models.IntegerField()
    quantity_rate = models.IntegerField()
    total = models.IntegerField()
    date_created = models.DateField(auto_now=True)
    type = models.ForeignKey(ServiceType, related_name="types", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="type", on_delete=models.CASCADE)

    class Meta:
        ordering = ('title_of_document',)
        verbose_name_plural = "Services"

    def __str__(self) -> str:
        return self.name

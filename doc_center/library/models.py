from django.db import models

from django.contrib.auth.models import User

# Create your models here.
#     
# documents
class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    no_of_volume = models.CharField(max_length=255, null=True)
    issued_to = models.CharField(max_length=255, null=True)
    borrower_signature = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)
    borrowed = models.BooleanField(default=False)
    issuing_officer = models.ForeignKey(User, related_name="books", on_delete=models.CASCADE, default=1)
    due_back = models.DateField(null=False)
    date_borrowed = models.DateField(null=False)
    date_returned = models.DateField(null = True)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = "Books"

    def __str__(self) -> str:
        return self.title

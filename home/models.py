from django.db import models

# Create your models here.
class IsbnRegister(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    language_of_book = models.CharField(max_length=100, null=False)
    editor = models.CharField(max_length=100, blank= True)
    book_type = models.CharField(max_length=100, blank=False)
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
    

class job_detail(models.Model):
    title = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=4000, blank= False)
    salary = models.IntegerField(blank= True)
    description = models.CharField(max_length=500, blank= False)
    
class CoverForm(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    language_of_book = models.CharField(max_length=100, null=False)
    editor = models.CharField(max_length=100, blank= True)
    book_type = models.CharField(max_length=100, blank=False)
    isbn_number = models.CharField(max_length=100, blank=False)
    def __str__(self) -> str:
        return f"{self.title} by {self.author} isbn- {self.isbn_number}"

class EditForm(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    language_of_book = models.CharField(max_length=100, null=False)
    book = models.FileField(upload_to='static')
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
    
class Pricing(models.Model):
    title = models.CharField(max_length=100, blank=False)
    budget = models.IntegerField(blank=False)
    description = models.CharField(max_length=500, blank= True)

    def __str__(self) -> str:
        return f"{self.title} on {self.budget}"
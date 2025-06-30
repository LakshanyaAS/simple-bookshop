from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,blank=True)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200,unique=True)
    genre=models.CharField(max_length=30)
    numpages=models.SmallIntegerField()    
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,related_name='books')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
class Book(models.Model):
    title  = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    year  = models.IntegerField()
    publisher = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        unique_together = (('title', 'author'),)      

class Attribute(models.Model):
    attribute = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.attribute       

class AttributeValue(models.Model):
    attribute_value = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.attribute_value          

class BookAttributeValue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title       

    class Meta:
        unique_together = (('book', 'attribute'),) 

from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return str(self.category_name)


class New(models.Model):
    new_name = models.CharField(max_length=64)
    new_description = models.TextField()
    new_photo = models.ImageField(upload_to='media')
    new_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    new_date = models.DateField()

    def __str__(self):
        return str(self.new_name)
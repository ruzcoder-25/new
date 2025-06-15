from django.db import models



class Author(models.Model):

    full_name = models.CharField(max_length=100)
    birthday = models.DateField()
    country = models.CharField(max_length=100)

    class Meta:

        db_table = 'author'
    def __str__(self):
        return self.full_name





class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    is_published = models.BooleanField(default=False)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.title













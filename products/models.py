from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    name = models.CharField(max_length=300)
    author = models.CharField(max_length=300, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    """
    Product Review Model
    """

    class Meta:
        ordering = ['-date_added']

    rating_selection = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )

    product = models.ForeignKey(Product,
                                related_name='reviews',
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL)
    user = models.ForeignKey(User,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    content = models.TextField()
    rating = models.IntegerField(choices=rating_selection, default=3)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

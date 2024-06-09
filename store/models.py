from django.db import models
from category.models import Category
from django.urls import reverse



class Product(models.Model):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField()
    image = models.ImageField(upload_to='images/products/')
    stock = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    UZ = "so'm"
    EN = "$"
    RU = "R"
    this_type = (
        (UZ, "so'm"),
        (EN, "$"),
        (RU, "R"),
    )
    price_type = models.CharField(
        max_length=100,
        choices=this_type,
        default="so'm",
    )


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])


    def __str__(self):
        return self.product_name
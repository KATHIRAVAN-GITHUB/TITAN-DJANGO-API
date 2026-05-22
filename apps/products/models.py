from django.db import models

class ProductCard(models.Model):
    producttitle = models.CharField(max_length=255)
    price = models.CharField(max_length=50)
    rating = models.FloatField(default=4.0)
    productimage = models.CharField(max_length=255)

    class Meta:
        db_table = "product_card"
        managed = False
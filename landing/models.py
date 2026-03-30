from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/category_imgs/', default="images/default.jpg")

    @property
    def goods_count(self):
        return self.goods.count()

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default="images/default.jpg")

class Good(models.Model):
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE, related_name='goods')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    car_model = models.OneToOneField(CarModel, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()

class Images(models.Model):
    image = models.ImageField(upload_to='images/goods/', default="images/default.jpg")
    good = models.ForeignKey(Good, on_delete=models.CASCADE, related_name='good', default=1)

    def __str__(self):
        return f'{self.id} | {self.good.title}'
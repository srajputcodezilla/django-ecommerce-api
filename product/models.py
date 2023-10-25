from django.db import models
import uuid

class Category(models.Model):
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, db_column="ctaegory_id", on_delete=models.SET_NULL, null=True)
    category_name=models.CharField(max_length=60,null=True,blank=True)
    price=models.IntegerField(null=True,blank=False,default=0)
    discount=models.IntegerField(null=True,blank=False,default=0)
    discount_type=models.CharField(max_length=10,null=True,blank=False)
    stock_qnt=models.IntegerField(null=True,blank=False,default=0)
    avilable_qnt=models.IntegerField(null=True,blank=False,default=0)
    class Meta:
        db_table = "products"
    def save(self, *args, **kwargs):
        # Automatically set the category_name field based on the associated Category's name
        if self.category:
            self.category_name = self.category.name
        super(Product, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
    
class ProductDetail(models.Model):
    product=models.OneToOneField(Product,on_delete=models.CASCADE, default=None)
    product_name=models.CharField(max_length=60,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    image_url=models.TextField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=False,default=0)
    class Meta:
        db_table = "details"
    def save(self, *args, **kwargs):
        # Automatically set the category_name field based on the associated Category's name
        print('\n ttt ->>>', self.product.name)
        # breakpoint()
        self.product_name = self.product.name
        self.product = self.product
        self.price = self.product.price
        self.description = self.description

        super(ProductDetail, self).save(*args, **kwargs)
    

    
    




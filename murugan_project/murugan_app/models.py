from django.db import models
# Signin model
class signin(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=13)
    password=models.CharField(max_length=100)

# Product model
class ecom_model(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="product_image/", blank=True, null=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0, null=True)

class Cart(models.Model):
    user = models.ForeignKey('signin', on_delete=models.CASCADE)  # Reference your custom sign_in model
    product = models.ForeignKey('ecom_model', on_delete=models.CASCADE)  # Reference your product model
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
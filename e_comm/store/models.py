from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 
    password = models.CharField(max_length=128)  
    phone_number = models.CharField(max_length=20, blank=True, null=True)  

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()  
    category = models.CharField(max_length=255, blank=True, null=True)
    imageUrl = models.CharField(max_length=2046)

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='carts', null=True, blank=True)
#     quantity = models.PositiveIntegerField(default=0)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    products = models.ManyToManyField(Product, through='CartProduct', related_name='carts')

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')
    shipping_address = models.TextField()
    billing_address = models.TextField()

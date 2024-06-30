from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

class Author(models.Model):
    
    name=models.CharField(max_length=200)
    
    age=models.IntegerField()
    
    place=models.CharField(max_length=200)
    
    created_date=models.DateTimeField(auto_now_add=True)
    
    updated_date=models.DateTimeField(auto_now=True)
    
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        
        return self.name
    
    
class Publisher(models.Model):
    
    name=models.CharField(max_length=200,unique=True)
    
    publication_date=models.DateField()
    
    created_date=models.DateTimeField(auto_now_add=True)
    
    updated_date=models.DateTimeField(auto_now=True)
    
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        
        self.name
        
        
class Language(models.Model):
    
    name=models.CharField(max_length=200,unique=True) #unique doubt
    
    created_date=models.DateTimeField(auto_now_add=True)
    
    updated_date=models.DateTimeField(auto_now=True)
    
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        
        return self.language
    
    
class Category(models.Model):
    
    name=models.CharField(max_length=200,unique=True)
    
    created_date=models.DateTimeField(auto_now_add=True)
    
    updated_date=models.DateTimeField(auto_now=True)
    
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        
        return self.name
    

class Book(models.Model):
    
    title=models.CharField(max_length=200,unique=True)
    
    description=models.TextField(null=True,blank=True)
    
    image=models.ImageField(upload_to='book_images',null=True,blank=True,default='book_images/default.jpg')
    
    price=models.PositiveBigIntegerField()
    
    isbnno=models.CharField(max_length=200,unique=True)
    
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    
    language=models.ManyToManyField(Language)
    
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    created_date=models.DateTimeField(auto_now_add=True)
    
    updated_date=models.DateTimeField(auto_now=True)
    
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        
        return self.title
    

class Basket(models.Model):
    
    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="cart")
    
    created_date=models.DateTimeField(auto_now_add=True)
    
    updated_date=models.DateTimeField(auto_now=True)
    
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        
        return self.owner.username


class BasketItem(models.Model):
    
    basket=models.ForeignKey(Basket,on_delete=models.CASCADE,related_name="cartitems")
    
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    
    language=models.ForeignKey(Language,on_delete=models.CASCADE)
    
    quantity=models.PositiveBigIntegerField(default=1)
    
    created_date=models.DateTimeField(auto_now_add=True)
    
    updated_date=models.DateTimeField(auto_now=True)
    
    is_active=models.BooleanField(default=True)
    
    is_order_placed=models.BooleanField(default=False)
    

class Order(models.Model):

    user_object = models.ForeignKey(
                                        User,
                                        on_delete=models.CASCADE, 
                                        related_name='myorders'
                                    )

    basket_item_objects = models.ManyToManyField(BasketItem)

    delivery_address = models.CharField(max_length=250)

    phone = models.CharField(max_length=12)

    pin=models.CharField(max_length=10,null=True)

    email = models.CharField(max_length=100)

    pay_options = (
        ('online', 'online'),
        ('cod', 'cod')
    )

    payment_mode = models.CharField(
                                        max_length=100, 
                                        choices=pay_options, 
                                        default='cod'
                                    )

    order_id = models.CharField(max_length=200, null=True)

    is_paid = models.BooleanField(default=False)

    order_status = (
        ('order_confirmed', 'Order confirmed'),
        ('dispatched', 'Dispatched'),
        ('in_transit', 'In transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),

    )

    status = models.CharField(
                                max_length=200, 
                                choices=order_status, 
                                default='order_confirmed'
                            )

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    


class Review(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    content = models.TextField()
    
    rating = models.PositiveIntegerField()  # range (e.g., 1-5)
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    updated_date = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)

    def __str__(self):
        
        return self.user.username

def create_basket(sender,instance,created,**kwargs):
    
    if created:
        
        Basket.objects.create(owner=instance)
        
post_save.connect(sender=User,receiver=create_basket)
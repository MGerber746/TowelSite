from django.db import models
from django.urls import reverse

# Create your models here.
# A Model that reflects a product category
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

# A model that reflects a product
class Product(models.Model):
    """
    Model representing a product
    """
    name = models.CharField(max_length=200)
    quickDescript = models.TextField(max_length=200, help_text='Enter a brief description of the product')
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the product')
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    origin = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='templates/products/%Y/%m/%d', blank = True)
    category = models.ManyToManyField(Category, help_text='Select a category for this product')
    stock = models.IntegerField()
    #slug = models.SlugField(unique=True)
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name


    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('product-detail', args=[str(self.id)])

# A Product instance (Not used this build)
class ProductInstance(models.Model):
    Product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    STATUS_CHOICES = (
        ('S', 'Sold'),
        ('I', 'In-Stock')
    )
    status = models.CharField(max_length = 2, choices = STATUS_CHOICES, null=True)

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} ({1})'.format(self.id,self.product.name)

# A Model that reflects an order
class Order(models.Model):
    Fname = models.CharField(max_length=200, null=False)
    Lname = models.CharField(max_length=200, null=False)
    Address = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False)
    postal_code = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    OrderDate = models.DateField(auto_now=True, auto_now_add=False)

    STATUS_CHOICES = (
        ('O', 'Ordered'),
        ('P', 'Paid'),
        ('S', 'Shipping'),
        ('R', 'Recieved')
    )
    status = models.CharField(max_length = 2, choices = STATUS_CHOICES, default='O')

    class Meta:
        ordering = ('-OrderDate',)

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} ({1})'.format(self.id,self.product.name)

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())

# A model that reflects an item in an order
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

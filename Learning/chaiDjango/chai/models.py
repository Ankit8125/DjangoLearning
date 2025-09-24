from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
  CHAI_TYPE_CHOICE = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
  ]
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to="chais/")
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
  description = models.TextField(default="") # TextField means it is compulsory to add a description
  
  def __str__(self):
    return self.name
  
# One to many
class ChaiReview(models.Model):
  chai = models.ForeignKey(ChaiVariety, on_delete= models.CASCADE, related_name= 'reviews') # Django automatically handles to which column we are making foreign key
  # The keyword "CASCADE" is used to automatically update or delete related records in other tables when a record is changed in a parent table:-
  # 1. Cascade on Delete:- When a record is deleted from a parent table, related records in child tables are also deleted.
  # 2. Cascade on Update:- When a record is updated in a parent table, the update is also applied to related records in child tables.
  
  user = models.ForeignKey(User, on_delete= models.CASCADE)
  rating = models.IntegerField()
  comment = models.TextField()
  date_added = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return f'{self.user.username} review for {self.chai.name}'
  
# Many to many
class Store(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  chai_varieties = models.ManyToManyField(ChaiVariety, related_name= "stores") # stores is how in other tables this field will be called
  
  def __str__(self):
    return self.name
  
# One to One
class ChaiCertificate(models.Model):
  chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name="certificate")
  certificate_number = models.CharField(max_length=100)
  issued_date = models.DateTimeField(default=timezone.now)
  valid_until = models.DateTimeField()
  
  def __str__(self):
    return f'Certificate for {self.name.chai}'
  
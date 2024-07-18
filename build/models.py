from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Ticket(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], blank=True)
    seats = models.CharField(max_length=100, blank=True)
    tr_id = models.CharField(max_length=50, blank=True)     
    amt = models.PositiveSmallIntegerField(blank=True)
    file = models.ImageField(upload_to='receipt/files/', blank=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

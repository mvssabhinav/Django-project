from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Event(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name=models.CharField( max_length=50)
    address=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    phone_number=models.IntegerField()
    event_name=models.CharField( max_length=50)
    venue=models.TextField()
    hall=models.CharField( max_length=50)
    event_date=models.DateTimeField(default=datetime.now)
    expected_cost=models.IntegerField()

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse("Event_detail", kwargs={"pk": self.pk})


class Birthday(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phone_no=models.IntegerField()
    capacity=models.IntegerField()
    No_of_chairs=models.IntegerField()
    catering=models.CharField( max_length=50)
    theam_decorators=models.CharField( max_length=50)
    game_host=models.CharField( max_length=50)
    magician=models.CharField( max_length=50)
    tatoo_artist=models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Birthday")
        verbose_name_plural = ("Birthdays")

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse("Birthday_detail", kwargs={"pk": self.pk})


class Marriage(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=50)    
    email=models.EmailField(max_length=254)
    phone_no=models.IntegerField()
    photographer=models.CharField( max_length=50)
    capacity=models.IntegerField()
    No_of_chairs=models.IntegerField()
    catering=models.CharField(max_length=50)
    theam_decorators=models.CharField(max_length=50)
    pre_wedding=models.CharField(max_length=50)
    mehandi_artist=models.CharField(max_length=50)
    bride_jewellery_rent=models.CharField( max_length=50)
    music_dance=models.CharField(max_length=50)
    invitation_gifts=models.CharField(max_length=50)
    status_message=models.CharField(max_length=255, blank=True,null=True)

    class Meta:
        verbose_name = ("Marriage")
        verbose_name_plural = ("Marriages")

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse("Marriage_detail", kwargs={"pk": self.pk})

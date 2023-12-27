from django.db import models
from django.contrib.auth.models import User


class Pipeline(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
# class Label(models.Model):
#     title = models.CharField(max_length=50)  

    

class CommonFields(models.Model):
    LABEL_CHOICES = (
        ('Hot', 'Hot'),
        ('Warm', 'Warm'),
        ('Cold', 'Cold'),
    )
    PHONE_CHOICES = (
        ('Work', 'Work'),
        ('Home', 'Home')
    )
    EMAIL_CHOICES = (
        ('Work', 'Work'),
        ('Home', 'Home')
    )
    VALUE_CHOICES = (
        ('Indian Rupee', 'Indian Rupee'),
        ('USD', 'USD'),
    )

    contact_person = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    # labels = models.ManyToManyField(Label,blank=True)
    labels = models.CharField(max_length=20, choices=LABEL_CHOICES, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Expected_close_date = models.DateField(blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    value_mode = models.CharField(max_length=50, choices=VALUE_CHOICES, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    phone_mode = models.CharField(max_length=50, choices=PHONE_CHOICES, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    email_mode = models.CharField(max_length=50, choices=EMAIL_CHOICES, blank=True, null=True)
    notes = models.TextField(blank= True)
    call = models.CharField(max_length=50, blank=True, null=True)
    activity = models.TextField(blank = True)
      

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Lead(CommonFields):
    pass  


class Deal(CommonFields):
    PIPELINE_CHOICES = (
        ('pipeline', 'pipeline'),
    )
    pipeline = models.CharField(max_length=50, choices=PIPELINE_CHOICES, blank=True)
    pipeline_status =models.ManyToManyField(Pipeline,blank=True)
    won = models.BooleanField(default = False)
    lost = models.BooleanField(default= False)

    def __str__(self):
        return self.title

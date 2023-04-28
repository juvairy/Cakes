from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator,MaxValueValidator

class Cakes(models.Models):
    name=models.CharField(max_length=25)
    shape_choices=[
        ("circle","circle"),
    ("rectangle","rectangle"),
    ("oval","oval"),
    ("customized","customized")
    ]
    customized=models.CharField(max_length=25,null=True,blank=True)
    shape=models.CharField(max_length=10,choices=shape_choices)
    layer_choices=[
        ("one","one"),
        ("two","two"),
        ("three","three")
    ]
    layers=models.CharField(max_length=10,choices=layer_choices)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    weight=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    def __str__(self):
        return self.name

class Carts(models.Model):
    name=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    qty=models.PositiveIntegerField(default=1)
class Orders(models.Model):
    name=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("shipped","shipped"),
        ("order-placed","order-placed"),
        ("in-transit","in-transit"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
        ("return","return")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    curDtae=datetime.date.today()
    expDate=curDtae+datetime.timedelta(days=5)
    expected_deliverydate=models.DateField(default=expDate)
    address=models.CharField(max_length=20,null=True)

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    comment=models.CharField(max_length=240)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.comment


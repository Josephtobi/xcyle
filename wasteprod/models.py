from django.db import models
from authentication.models import User

# Create your models here.

    

    
#Item model, for storing different items to be sold



class Waste(models.Model):

    CATEGORY_CHOICES = (
        ('paper','Paper'),
        ('plastics','Plastics'),
        ('metal','Metal'),
        ('glass','Glass'),
    )

    title = models.CharField(max_length=100)
    asking_price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    description = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    is_sold=models.BooleanField(default=False)
    seller = models.ForeignKey(to=User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Bid(models.Model):
    bidding_price = models.FloatField()
    buyer = models.ForeignKey(to=User,on_delete=models.CASCADE)
    prod = models.ForeignKey(to=Waste,on_delete=models.CASCADE,related_name='bids')
    bid_won=models.BooleanField(default=False)

    def __str__(self):
        go=str(self.bidding_price)
        return go




    


#Order Item, checks on a particular item if ordered



#Order Model, Details on the Order made



#Address Model



#Payment Model Using stripe



#Coupon Model


#Refund Model




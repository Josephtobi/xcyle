from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from wasteprod.models import Waste,Bid



class BidSerializer(serializers.ModelSerializer):
    

    
    

    class Meta:
        model=Bid
        fields=('bidding_price','prod')
        



class WasteSerializer(serializers.ModelSerializer):

    bids= BidSerializer(read_only=True,many=True)
    
    

    class Meta:
        model=Waste
        fields=('id','title','asking_price','category','description','bids')



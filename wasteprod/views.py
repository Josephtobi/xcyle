
from django.http import request
from django.shortcuts import render
from wasteprod.models import Bid, Waste
from rest_framework import serializers
from rest_framework.generics import CreateAPIView,ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from wasteprod.serializers import BidSerializer, WasteSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class WasteOwnerList(ListCreateAPIView):
    serializer_class=WasteSerializer

    permission_classes=(IsAuthenticated,)

    #overrides default setting and add owner field to model being saved
    def perform_create(self, serializer):
        return serializer.save(seller=self.request.user)

    #override default and only query for objects by owner
    def get_queryset(self):
        return Waste.objects.filter(seller=self.request.user)




class WasterOwnerDetail(RetrieveUpdateDestroyAPIView):
    serializer_class=WasteSerializer

    permission_classes=(IsAuthenticated,)
    lookup_field='id'

    def get_queryset(self):
        return Waste.objects.filter(seller=self.request.user)#prod=waste_set)



class WasteListAPIView(ListAPIView):
    serializer_class=WasteSerializer

    permission_classes=(IsAuthenticated,)

    queryset=Waste.objects.all()

class WasteDetailAPIView(RetrieveAPIView):
    serializer_class=WasteSerializer

    permission_classes=(IsAuthenticated,)

    lookup_field='id'

    def get_queryset(self):
        return Waste.objects.all()


    


class BidCreateAPIView(CreateAPIView):

    serializer_class=BidSerializer

    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
    
        
        return serializer.save(buyer=self.request.user)


class BidOwnersListAPIView(ListAPIView):
    serializer_class=BidSerializer

    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        return Bid.objects.filter(buyer=self.request.user)
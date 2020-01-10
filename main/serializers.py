from rest_framework import serializers
from .models import product

class productSerializer(serializers.ModelSerializers):

    class Meta:
        model =product
        fields ='__all__'

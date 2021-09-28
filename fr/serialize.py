from fr import models
from rest_framework import routers, serializers, viewsets

class OprosSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Opros
        fields = '__all__'

class VoprosSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Vopros
        fields = '__all__'

class OtvetSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Otvet
        fields = '__all__'

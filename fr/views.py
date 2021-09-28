import datetime

from django.shortcuts import render
from fr import models
from fr import serialize

from rest_framework import routers, serializers, viewsets, views
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics
from django.http import Http404
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.


class OprosViewList(viewsets.ModelViewSet):
    queryset = models.Opros.objects.all()
    serializer_class = serialize.OprosSer
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        opros = self.get_object()
        if opros.start is not None:
            serializer.validated_data['start'] = opros.start
        serializer.save()

class VoprosViewList(viewsets.ModelViewSet):
    queryset = models.Vopros.objects.all()
    serializer_class = serialize.VoprosSer
    permission_classes = [IsAdminUser]

class OtvetViewList(viewsets.ModelViewSet):
    queryset = models.Otvet.objects.all()
    serializer_class = serialize.OtvetSer
    permission_classes = [IsAdminUser]

class OprosViewReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = models.Opros.objects.filter(start__lte=datetime.datetime.now(), finish__gte=datetime.datetime.now())
    serializer_class = serialize.OprosSer

class VoprosViewReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = models.Vopros.objects.filter(opros__start__lte=datetime.datetime.now(), opros__finish__gte=datetime.datetime.now())
    serializer_class = serialize.VoprosSer

class SetOtvet(viewsets.ModelViewSet):
    queryset = models.Otvet.objects.all()
    serializer_class = serialize.OtvetSer


    def get_queryset(self):
        print(f'self.request.user.id {self.request.user.id}')
        if self.request.user.is_authenticated:
            return models.Otvet.objects.filter(user_id=self.request.user.id)
        else:
            return models.Otvet.objects.all()


class LoginView(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

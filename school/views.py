from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = userserializer

    def list(self, request, *args, **kwargs):
        student = request.query_params.get('user', None)
        if student:
            self.queryset = self.queryset.filter(uquvchi=student)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        related_users = Users.objects.filter(user=instance.user).exclude(id=instance.id)[:5]
        related_serializer = userserializer(related_users, many=True)
        return Response({
            'product': serializer.data,
            'related_products': related_serializer.data
        })


class DailyViewSet(viewsets.ModelViewSet):
    queryset = Daily.objects.all()
    serializer_class = dailyserializer


class ThoughtsViewSet(viewsets.ModelViewSet):
    queryset = Thoughts.objects.all()
    serializer_class = thoughtserializer




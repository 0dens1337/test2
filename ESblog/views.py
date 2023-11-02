from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ESblog
from .serializers import ESblogSerializer


class ESblogAPIView(APIView):
    def get(self, request):
        lst = ESblog.objects.all().values()
        return Response({'title': 'list(lst)'})

    def post(self, request):
        return Response({'title': 'Kan Kan'})


#class ESblogAPIView(generics.ListAPIView):
#   queryset =ESblog.objects.all()
#   serializer_class = ESblogSerializer
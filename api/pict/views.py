from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from .models import Works
from .serializers import (WorksSerializer, SingleWorksSerializer, UpdateWorkImageSerializer)


class WorksListView(generics.ListAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer

class WorksDetailView(generics.RetrieveAPIView):
    queryset = Works.objects.all()
    serializer_class = SingleWorksSerializer

class UpdateWorkImage(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UpdateWorkImageSerializer
    queryset = Works.objects.all()
    lookup_field = 'pk'



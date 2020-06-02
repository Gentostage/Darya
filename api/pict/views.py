from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework import generics

from .models import Works, Pictures
from .serializers import (WorksSerializer, SingleWorksSerializer, UpdateWorkImageSerializer, DestroyCreateImageSerializer)


class WorksListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Works.objects.all().order_by('-id')
    serializer_class = WorksSerializer

class WorksDetailView(generics.RetrieveAPIView):
    queryset = Works.objects.all()
    serializer_class = SingleWorksSerializer

class UpdateWorkImage(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UpdateWorkImageSerializer
    queryset = Works.objects.all()
    lookup_field = 'pk'

class DestroyImage(generics.DestroyAPIView):
    serializer_class = DestroyCreateImageSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Pictures.objects.all()
    lookup_field = 'pk'




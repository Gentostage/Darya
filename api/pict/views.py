from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics

from .models import Works
from .serializers import (WorksSerializer, SingleWorksSerializer, UpdateWorkImageSerializer)


class WorksListView(generics.ListCreateAPIView):
    queryset = Works.objects.all().order_by('-id')
    serializer_class = WorksSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class WorksDetailView(generics.RetrieveAPIView):
    queryset = Works.objects.all()
    serializer_class = SingleWorksSerializer

class UpdateWorkImage(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UpdateWorkImageSerializer
    queryset = Works.objects.all()
    lookup_field = 'pk'



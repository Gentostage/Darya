from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from .models import Works
from .serializers import (WorksSerializer, SingleWorksSerializer, UpdateWorkImageSerializer)


class WorksView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        queryset = Works.objects.all()
        serializer = WorksSerializer(queryset, many=True)
        return Response({'works': serializer.data})


class SingleWorksView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, id):
        queryset = Works.objects.filter(id=id)
        serializer = SingleWorksSerializer(queryset, many=True)
        return Response({'work': serializer.data})

class UpdateWorkImage(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UpdateWorkImageSerializer
    queryset = Works.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.kwargs['id'])
        self.check_object_permissions(self.request, obj)
        return obj



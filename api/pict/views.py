from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Works
from .serializers import (WorksSerializer, WorksPOSTSerializer, SingleWorksSerializer)


class WorksView(APIView):
    # permission_classes = [IsAuthenticated, ]
    permission_classes = [AllowAny, ]

    def get(self, request):
        queryset = Works.objects.all()
        serializer = WorksSerializer(queryset, many=True)
        return Response({'works': serializer.data})

    def post(self, request):
        if request.user.is_authenticated:
            serializer = WorksPOSTSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            else:
                return Response(status=400)
        else:
            return Response(status=401)


class SingleWorksView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, id):
        queryset = Works.objects.filter(id=id)
        serializer = SingleWorksSerializer(queryset, many=True)
        return Response({'work': serializer.data})

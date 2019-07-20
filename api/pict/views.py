from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Works
from .serializers import WorksSerializer


class WorksView(ListAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer


class SingleWorksView(RetrieveUpdateDestroyAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer

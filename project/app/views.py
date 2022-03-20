from rest_framework import viewsets

from project.app.models import ExampleModel
from project.app.serializers import ExampleSerializer


class ExampleViewSet(viewsets.ModelViewSet):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer

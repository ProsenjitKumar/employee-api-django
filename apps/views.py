from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import Employeer


class HomeView(TemplateView):
    template_name = 'index.html'


class EmployeerView(viewsets.ModelViewSet):
    queryset = Employeer.objects.all()
    serializer_class = EmployeeSerializer

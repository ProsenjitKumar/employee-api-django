from rest_framework import serializers
from .models import Employeer


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employeer
        fields = ('id', 'name', 'log_date', 'log_time', 'login', 'logout')



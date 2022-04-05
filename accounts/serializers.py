from rest_framework import serializers
from accounts.models import Routine

class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = (
            'id'
            'description',
            'time',
            'is_complete',
        )
from rest_framework import serializers

from accounts.models import UserRoutine


class UserRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoutine
        fields = (
            'id',
            'content',
            'is_completed',
            'imitated_user',
            'celebrity',
        )
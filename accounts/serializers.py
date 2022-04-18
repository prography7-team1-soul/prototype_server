from rest_framework import serializers

from accounts.models import UserRoutine, User


class UserRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoutine
        fields = (
            'id',
            'content',
            'is_completed',
        )

    def create(self, validated_data):
        validated_data["imitated_user"] = self.context.get("request").user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["imitated_user"] = self.context.get("request").user
        return super().update(instance, validated_data)

class RoutineSummarizeSerializer(serializers.ModelSerializer):
    routines = UserRoutineSerializer(read_only=True, many=True)
    class Meta:
        model = UserRoutine
        fields = (
            'routines',
            'celebrity',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'uuid',
        )
        read_only_fields = ('id', 'uuid',)

    def create(self, validated_data):
        header = self.context.get("request").headers
        uuid = header.get("uuid", None)
        validated_data["uuid"] = uuid
        return super().create(validated_data)
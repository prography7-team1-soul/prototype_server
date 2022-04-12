from rest_framework import serializers

from accounts.models import UserRoutine, User


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
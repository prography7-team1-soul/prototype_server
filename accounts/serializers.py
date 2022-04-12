from rest_framework import serializers

from accounts.models import UserRoutine, User
from celebrities.models import Celebrity


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

class CelebrityNicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = (
            'name',
        )

class RoutineSummarizeSerializer(serializers.ModelSerializer):
    routines = UserRoutineSerializer(read_only=True, many=True)
    celebrity = CelebrityNicknameSerializer(read_only=True)
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
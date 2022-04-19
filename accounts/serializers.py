from rest_framework import serializers

from accounts.models import UserRoutine, User


class UserRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoutine
        fields = (
            'id',
            'time',
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
        request = self.context.get("request")
        uuid = request.headers.get("uuid", None)
        user = User.objects.filter(uuid=uuid).first()
        if user:
            raise serializers.ValidationError({'error_message':'가입된 유저가 존재합니다.'})
        validated_data["uuid"] = uuid
        return super().create(validated_data)
from rest_framework import serializers
from accounts.models import UserRoutine
from celebrities.models import Celebrity, CelebrityJob, CelebrityRoutine


class CelebrityJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = CelebrityJob
        fields = (
            'name',
            'background_color',
            'text_color',
        )

class CelebrityRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CelebrityRoutine
        fields = (
            'id',
            'time',
            'content',
        )
class CelebritySerializer(serializers.ModelSerializer):
    job = CelebrityJobSerializer(read_only=True)
    celebrity_routines = CelebrityRoutineSerializer(read_only=True, many=True)
    class Meta:
        model = Celebrity
        fields = (
            'id',
            'name',
            'english_name',
            'image',
            'job',
            'MBTI',
            'nationality',
            'introduction',
            'body_spec',
            'education',
            'wise_saying',
            'wealth',
            'spouse',
            'children',
            'celebrity_routines',
            'age',
            'birthday',
            'deceased_at',
            'tmi',
        )
        read_only_fields = (
            'id',
            'name',
            'english_name',
            'image',
            'job',
            'MBTI',
            'nationality',
            'introduction',
            'body_spec',
            'education',
            'wise_saying',
            'wealth',
            'spouse',
            'children',
            'celebrity_routines',
            'age',
            'birthday',
            'deceased_at',
            'tmi',
        )

class CelebritySummarizeSerializer(serializers.ModelSerializer):
    job = CelebrityJobSerializer(read_only=True)
    class Meta:
        model = Celebrity
        fields = (
            'id',
            'name',
            'english_name',
            'image',
            'job',
            'nationality',
        )

class ImitateRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoutine
        fields = (
            'imitated_user',
            'celebrity_name',
        )
        read_only_fields = (
            'imitated_user',
            'celebrity_name',
        )

    def create(self, validated_data):
        celebrity = self.context.get('celebrity')
        imitated_user = self.context.get('request').user

        for celebrity_routine in celebrity.celebrity_routines.all():
            user = UserRoutine.objects.create(content=celebrity_routine.content, time = celebrity_routine.time, imitated_user=imitated_user, celebrity=celebrity)
        return user
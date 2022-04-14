from rest_framework import serializers
from accounts.models import UserRoutine
from celebrities.models import Celebrity, CelebrityJob

class CelebrityJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = CelebrityJob
        fields = (
            'name',
            'background_color',
            'text_color',
        )

class CelebritySerializer(serializers.ModelSerializer):
    job = CelebrityJobSerializer(read_only=True)
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
        celebrity_routines = celebrity.celebrity_routines
        for routine in celebrity_routines.items():
            user = UserRoutine.objects.create(content=routine, imitated_user=imitated_user, celebrity=celebrity)
        return user
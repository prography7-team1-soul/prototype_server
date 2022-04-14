from rest_framework import serializers

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
            'deceased_at'
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
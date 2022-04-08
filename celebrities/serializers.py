from rest_framework import serializers

from celebrities.models import Celebrity


class CelebritySerializer(serializers.ModelSerializer):
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
            'wealth',
            'spouse',
            'children',
            'celebrity_routines',
            'age',
            'birthday',
            'deceased_at'
        )

class CelebritySummarizeSerializer(serializers.ModelSerializer):
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


from rest_framework import serializers

from celebrities.models import Celebrity, Routine


class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = (
            'id',
            'name',
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
            'age',
            'birthday',
            'deceased_at'
        )


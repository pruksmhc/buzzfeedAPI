from rest_framework import serializers
from buzzfeedAPI.model import Result, LANGUAGE_CHOICES, STYLE_CHOICES


class BuzzfeedSerializer(serializers.Serializer):
    data = serializers.CharField(require=True)
    date = serializers.DateTimeField(require=True)
 

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Buzzfeed.objects.create(**validated_data)

  
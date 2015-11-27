from rest_framework import serializers
from buzzfeed.models import BuzzfeedSearch


class BuzzfeedSerializer(serializers.Serializer):
	json= serializers.CharField(required=False,  allow_blank=True, max_length=100), 
	date= serializers.CharField(required=False, allow_blank=True, max_length=100)
	user = serializers.CharField(required=False, allow_blank=True, max_length=100)
#this defines the fields that get serialized/deserialized. 

	def create(self,  validated_data): 
	#define how instance sar ecreated. 
		return BuzzfeedSearch.objects.create(**validated_data)


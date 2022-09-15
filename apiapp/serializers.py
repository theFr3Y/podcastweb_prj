'''
Serializers allow complex data such as querysets and model instances to be
converted to native Python datatypes that can then be easily rendered
into JSON, XML or other content types.
Serializers also provide deserialization, allowing parsed data to be
converted back into complex types, after first validating the incoming data.
'''

from rest_framework import serializers
from mainapp.models import PodcastModel, PodcasterModel

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastModel
        fields = '__all__'
        
class PodcasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcasterModel
        fields = '__all__'
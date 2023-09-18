from rest_framework import serializers
from electionApp.models import *


class PartyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyData
        fields = ('__all__')

class CondidateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondidateData
        fields = ('__all__')
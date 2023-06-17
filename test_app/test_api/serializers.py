from rest_framework import serializers
from test_api.models import Participant, IQTestResult, EQTestResult


class ParticipantSerializer(serializers.ModelSerializer):
    login = serializers.CharField(read_only=True)

    class Meta:
        model = Participant
        fields = ['login', 'id']


class IQTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = IQTestResult
        fields = ('score', 'time_taken')


class EQTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = EQTestResult
        fields = ('letters', 'time_taken')

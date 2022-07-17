from rest_framework import serializers

from core.helper.constants import PageInfo
from core.flight.models import FlightDetails


class FlightDetailsSerializer(serializers.ModelSerializer):
    source = serializers.StringRelatedField()
    destination = serializers.StringRelatedField()

    class Meta:
        model = FlightDetails
        fields = ['id', 'flight_number', 'source', 'destination', 'price', 'departure_date_time', 'arrival_date_time']
        # fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation


class FlightsListSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    p_no = serializers.IntegerField(required=False, default=PageInfo.p_no)
    p_size = serializers.IntegerField(required=False, default=PageInfo.p_size)
    sort = serializers.ListField(required=False, default=[],
                                 child=serializers.DictField(required=True))

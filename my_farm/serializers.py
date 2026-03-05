from rest_framework import serializers
from .models import *

class FarmHandSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmHand
        fields = ['id', 'username', 'phone', 'certification_number']


class FarmSerializer(serializers.ModelSerializer):
    farmhand_details = FarmHandSerializer(source='farmhand', read_only=True)

    class Meta:
        model = Farm
        fields = ['id', 'name', 'farmhand', 'farmhand_details', 'location', 'gps_coordinates', 'created_at']


class TreatmentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentLog
        fields = ['id', 'batch', 'date', 'action_type', 'product_used', 'notes']


class BatchSerializer(serializers.ModelSerializer):
    treatment_history = TreatmentLogSerializer(many=True, read_only=True, source='treatment_logs')
    farm_name = serializers.ReadOnlyField(source='farm.name')

    class Meta:
        model = Batch
        fields = [
            'id', 'farm', 'farm_name', 'crop_name', 'variety', 
            'planted_date', 'harvest_date', 'quantity_kg', 
            'destination', 'qr_generated', 'treatment_history', 'created_at'
        ]
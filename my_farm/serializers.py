from rest_framework import serializers
from .models import *

class FarmHandSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmHand
        fields = [ 'username', 'phone', 'certification_number']


class FarmSerializer(serializers.ModelSerializer):
    farmhand_details = serializers.CharField(source='farmhand.__str__', read_only=True)
    class Meta:
        model = Farm
        fields = [ 'name', 'farmhand_details', 'location', 'gps_coordinates', 'created_at']


class TreatmentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentLog
        fields = [ 'batch', 'date', 'action_type', 'product_used', 'notes']


class BatchSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source='farm.__str__', many = True , readonly = True)

    class Meta:
        model = Batch
        fields = [
            'farm_name', 'crop_name', 'variety', 
            'planted_date', 'harvest_date', 'quantity_kg', 
            'destination', 'qr_generated', 'created_at'
        ]
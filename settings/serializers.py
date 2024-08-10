from rest_framework import serializers

class SettingsSerializer(serializers.Serializer):
    free_shipping_above = serializers.IntegerField()
    delivery_charges = serializers.IntegerField()
    phone_number = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    timings = serializers.CharField(max_length=255)
    headline = serializers.CharField(max_length=255)
    items_per_page = serializers.IntegerField()

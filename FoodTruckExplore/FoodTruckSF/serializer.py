from rest_framework import serializers

class FoodTruckSerializer(serializers.Serializer):
    _id = serializers.IntegerField()
    applicant = serializers.CharField(max_length=255)
    facility_type = serializers.CharField(max_length=100, required=False)
    address = serializers.CharField(max_length=255, required=False)
    status = serializers.CharField(max_length=100, required=False)
    food_items = serializers.CharField(required=False)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    schedule = serializers.URLField(max_length=1024, required=False)
    approved = serializers.DateTimeField()
    expiration_date = serializers.DateTimeField()
    distance = serializers.FloatField(required=False)

    def to_representation(self, instance):
        """Modify the representation of the serializer to expose 'id' without underscore."""
        ret = super().to_representation(instance)  # Get the original representation
        ret['id'] = ret.pop('_id', None)  # Rename '_id' to 'id'
        dist = ret.pop("distance", None)
        if dist:
            ret["distance"] = round(dist / 1000, 2)
        return ret

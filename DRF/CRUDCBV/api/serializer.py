from rest_framework import serializers
from api.models import Student

class studentSeralizer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance

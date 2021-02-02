from customUser.models import MyUser
from .models import Coordinates
from rest_framework import serializers
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer) :
    password = serializers.CharField(write_only=True)
    class Meta :
        model = MyUser
        fields = ('email', 'user_name', 'first_name', 'last_name', 'city', 'password')


    def create(self, validated_data) :
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        user.is_active = False
        return user

class CoordinateSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Coordinates
        fields = '__all__'
        # depth = 1
        read_only_fields = ("created_at", "person", )

    def validate_lattitude (self, value) :
        if value > 90 or value < -90 :
            raise serializers.ValidationError("Latitude value must be between -90 and 90 degrees")
        else :
            return value

    def validate_longitude (self, value) :
        if value > 180 or value < -180 :
            raise serializers.ValidationError("Latitude value must be between -180 and 180 degrees")
        else :
            return value


    def create(self, validated_data) :
        validated_data['person'] = self.context['request'].user
        obj = super().create(validated_data)
        obj.created_at = timezone.now()
        obj.save()
        return obj


class CoordinateInfoSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Coordinates
        fields = '__all__'
        depth = 1

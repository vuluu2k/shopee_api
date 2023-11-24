from .models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):

    def validate_password(self, value):
        if value.isalnum():
            raise serializers.ValidationError(
                'password must have atleast one special character.')
        return value

    # def validate(self, data):
    #     if data['first_name'] == data['last_name']:
    #         raise serializers.ValidationError("first_name and last_name shouldn't be same.")
    #     return data

    # def to_internal_value(self, data):
    #     user_data = data['user']
    #     return super().to_internal_value(user_data)

    class Meta:
        model = Profile
        exclude = ['password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

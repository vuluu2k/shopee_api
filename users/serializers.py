from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User, BankCard


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCard
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    banks = serializers.SerializerMethodField()

    def validate_password(self, value):
        if value.isalnum():
            raise serializers.ValidationError(
                'password must have at least one special character.')
        return make_password(value)

    # def validate(self, data):
    #     if data['first_name'] == data['last_name']:
    #         raise serializers.ValidationError("first_name and last_name shouldn't be same.")
    #     return data

    # def to_internal_value(self, data):
    #     user_data = data['user']
    #     return super().to_internal_value(user_data)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'avatar', 'password', 'banks', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_banks(self, obj):
        bank_query = BankCard.objects.filter(user_id=obj.id)
        serializer = BankSerializer(bank_query, many=True)

        return serializer.data

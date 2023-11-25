from .models import User, BankCard
from rest_framework import serializers


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
        return value

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
                  'last_name', 'email', 'avatar', 'banks']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_banks(self, obj):
            bank_query = BankCard.objects.filter(user_id=obj.id)
            serializer = BankSerializer(bank_query, many=True)
    
            return serializer.data

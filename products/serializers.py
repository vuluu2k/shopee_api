from rest_framework import serializers
from .models import Product, Feedback, Variation
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = '__all__'

class GeneralProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image','images', 'category', 'price', 'slug', 'feedbacks' ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class DetailProductSerializer(serializers.ModelSerializer):
    feedbacks = FeedbackSerializer(many=True, read_only=True)
    variations = VariationSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

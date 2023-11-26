from rest_framework import serializers
from .models import Product, Feedback
class FeedbackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feedback
        fields = '__all__'

class GeneralProductSerializer(serializers.ModelSerializer):
    feedbacks = FeedbackSerializer(many=True, read_only=True)    
    class Meta:
        model = Product
        fields = ['id','price','feedbacks']

class DetailProductSerializer(GeneralProductSerializer):
    feedbacks = FeedbackSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id','feedbacks']



# class ProductSerializer(serializers.ModelSerializer):
#     variations = VariationSerializer(many=True, read_only=True)
#     feedbacks = FeedbackSerializer(many=True, read_only=True)

#     class Meta:
#         model = Product
#         fields = ['id', 'price', 'feedbacks']
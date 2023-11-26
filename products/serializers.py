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

# from rest_framework import serializers
# from .models import Product, Variation, Feedback

# class VariationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Variation
#         fields = '__all__'

# class FeedbackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Feedback
#         fields = '__all__'

# class ProductSerializer(serializers.ModelSerializer):
#     variations = VariationSerializer(many=True, read_only=True)
#     feedbacks = FeedbackSerializer(many=True, read_only=True)

#     class Meta:
#         model = Product
#         fields = ['id', 'price', 'feedbacks']
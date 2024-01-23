from rest_framework import serializers
from django.db.models import Sum, Avg

from .models import Product, Feedback, Variation, OrderDetail
from users.models import User
class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'avatar']
        ref_name = 'ProductUser'

class FeedbackSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Feedback
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
    total_sold = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [f.name for f in Product._meta.get_fields()] + ['total_sold', 'average_rating']

    def get_total_sold(self, obj):
        return OrderDetail.objects.filter\
            (variation__product=obj, order__status=2).aggregate(total=Sum('quantity'))['total']

    def get_average_rating(self, obj):
        return Feedback.objects.filter(product=obj).aggregate(average=Avg('star'))['average']
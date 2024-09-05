from rest_framework import serializers
from .models import Cart
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
=======
    # Use ProductSerializer for read operations, PrimaryKeyRelatedField for writes
>>>>>>> f64aa0f6b8066712aa175e12ac398d819ee1771a
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Cart
        fields = '__all__'

    def to_representation(self, instance):
        # Override the output to use the nested ProductSerializer for the product field
        response = super().to_representation(instance)
        response['product'] = ProductSerializer(instance.product).data
        return response
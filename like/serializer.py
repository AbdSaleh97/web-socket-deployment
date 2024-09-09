from rest_framework import serializers
from .models import Like

# Absolute imports from the relevant apps
from store.serializer import StoreSerializer
from product.serializers import ProductSerializer
from idea.serializer import IdeaSerializer
from report.serializers import ReportSerializer

from store.models import Store
from idea.models import Idea
from product.models import Product
from report.models import Report

class LikeSerializer(serializers.ModelSerializer):
    content_object = serializers.SerializerMethodField()

    class Meta:
        model = Like
        fields = ['id', 'user', 'content_type', 'object_id', 'created_at', 'content_object']

    def get_content_object(self, obj):
        if isinstance(obj.content_object, Store):
            return StoreSerializer(obj.content_object).data
        elif isinstance(obj.content_object, Product):
            return ProductSerializer(obj.content_object).data
        elif isinstance(obj.content_object, Idea):
            return IdeaSerializer(obj.content_object).data
        elif isinstance(obj.content_object, Report):
            return ReportSerializer(obj.content_object).data
        return None

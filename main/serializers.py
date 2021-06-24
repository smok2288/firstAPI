from rest_framework import serializers

from main.models import ProductModel


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150, read_only=True)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class ProductSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150, read_only=True)
    product = ProductSerializer()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance

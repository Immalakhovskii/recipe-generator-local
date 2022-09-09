from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from users.serializers import CustomUserSerializer
from recipes.models import (Tag, Ingredient, Recipe, IngredientAmount,
                            Favorite, ShoppingCartItem)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')


class IngredientAmountSerializer(IngredientSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['amount'] = (
            IngredientAmount.objects.filter(ingredient=instance)
            .values('amount')[0]['amount']
        )
        return representation


class RecipeReadSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    author = CustomUserSerializer(read_only=True)
    ingredients = IngredientAmountSerializer(read_only=True, many=True)
    image = Base64ImageField()
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ('id', 'tags', 'author', 'ingredients', 'name',
                  'text', 'image', 'cooking_time',
                  'is_favorited', 'is_in_shopping_cart')

    def get_is_favorited(self, obj):
        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
        if user is None or user.is_anonymous:
            return False
        return Favorite.objects.filter(
            fan=user, favorite_recipe=obj).exists()

    def get_is_in_shopping_cart(self, obj):
        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
        if user is None or user.is_anonymous:
            return False
        return ShoppingCartItem.objects.filter(
            client=user, recipe_to_cart=obj).exists()